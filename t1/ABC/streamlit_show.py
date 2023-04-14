import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

st.set_page_config(page_title="数据分析板块", page_icon=":柱状图", layout="wide")


df = pd.read_excel('设备台帐信息2022.11.08.xls')


# print(df.columns)



使用部门 = st.sidebar.selectbox(
    "选择使用部门:",
    options=df['使用部门'].unique(),
)
# df1 是根据选择之后的查询结果
df1 = df.query(
    "使用部门 == @使用部门"
)

当前管理状态 = st.sidebar.selectbox(
    "当前管理状态:",
    options=df1['当前管理状态'].unique(),
)

制造厂 = st.sidebar.multiselect(
    "制造厂:",
    options=df1['制造厂'].unique(),
    default=df1['制造厂'].unique()
)


df_selection = df.query(
    "使用部门 == @使用部门 & 当前管理状态 == @当前管理状态 &制造厂 == @制造厂"
)

dic = {'完好':0,'不完好':0}
完好状态series = df_selection["完好状态"].value_counts()
for i in 完好状态series.index:
    dic[i] = 完好状态series[i]


dic1 = {'生产':0,'非生产':0}
生产状态series = df_selection["生产用途"].value_counts()
for i in 生产状态series.index:
    if i == '生产':
        dic1[i] =  生产状态series[i]
    if i == '非生产':
        dic1[i] =  生产状态series[i]




st.title("设备数据看板")
st.markdown("----")
total_sales = int(df_selection["单价(元)"].sum())


left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("总价值:")
    st.subheader("￥{}".format(total_sales))

with middle_column:
    st.subheader("完好状态:")
    st.subheader("完好：{}，不完好: {}".format(dic['完好'],dic['不完好']))


with right_column:
    st.subheader("生产状态:")
    st.subheader("生产：{}，非生产: {}".format(dic1["生产"],dic1["非生产"]))

sales_by_product_line = (
    df_selection.groupby(by=["设备名称"]).sum()[["单价(元)"]].sort_values(by="单价(元)")
)

fig_product_sales = px.bar(
    sales_by_product_line,
    y="单价(元)",
    x=sales_by_product_line.index,
    title="<b>设备单价</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    
)

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


complete_line = (
    df_selection['完好状态'].value_counts()
)

完好状态_df = pd.DataFrame(complete_line)
# print(complete_line)
fig_complete = px.bar(
    完好状态_df,
    y = '完好状态',
    x=完好状态_df.index,
    title="<b>设备完好状态</b>",
    color_discrete_sequence=["#0083B8"] * len(complete_line),
    
)

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


fig_complete.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)




left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_product_sales, use_container_width=True)
right_column.plotly_chart(fig_complete, use_container_width=True)

use_line = (
    df_selection['生产用途'].value_counts()
)

生产用途_df = pd.DataFrame(use_line)

fig_use = px.bar(
    生产用途_df,
    y = '生产用途',
    x=生产用途_df.index,
    title="<b>设备用途</b>",
    color_discrete_sequence=["#0083B8"] * len(use_line),
    
)




left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_use, use_container_width=True)

