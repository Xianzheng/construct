#   .第一阶段：项目主要思路，运行build 文件夹下的 building.py
#   根据draw/drawModels.txt会生成数据库字段信息
#   信息自动生成url，models，views,forms等关键信息
#   配合上提前做好的templates，可提供堆数据库做增删改查

#   .第二阶段：build文件夹会生成一个主项目，并带有一个主APP
#   这个主APP利用APP中的mystatic/building可根据drawModels.txt生成若干个子APP
#   这些子APP可处理不同场景的应用，比如BOM结构应用（人力资源管理，MES)
#   由于这些子APP有较强的服务器做后台，或者各个APP目很容易做成主项目
#   在不损失template 功能的情况下，让template 更美观，UI更容易操作

#   第三阶段主APP可根据选择生成不同结构的APP
#   流程结构，服务器运用（待开发）


# 具体细节记录
#.怎么使用call_command

from django.core.management import call_command

call_command("makemigrations")

call_command("migrate")

#.CSS使用justify - content，display：flex; 

# template直接用bootstap4.1网上下下的安装包，解压后放在
# building 的mystatic 的 bootstrap下 分css文件夹，js文件夹

# 支持 bootstrap 的 jquery.js在网上另外下载·放在 building/mystatic/bootstarp下

# 由于bootstrap的代码过于多用prettier调节格式比较方便

#选中调节的代码 ctrl + shift + p 搜索 formmat

'''

2023/3/2
写script脚本一定要写成<script></script>

加入corsheaders,做一些修改

上传应该有两种方法一种通过form提交还有fetch/ajax,比较熟悉
fetch就用fetch这个应该还能加强

由于在template中html应该不是传统的html,所以提交的时候需要加上csrf token
如果用前后端分离的形式提交则不用（后面待测试）
在template中自带 {{csrf_token}}

在template中提交数据,也就是django整体一体化
可分为form提交或fetch/ajax提交,都需在html中有 
{% csrf_token %}/{{token_token}}的出现



'''

'''

#添加不用修改程序 自动创建项目内置完善的setting js,jquery,bootstrap
'''

'''
parsing view 肯定要改
没有float:left视图显示不出来
drawModel的逗号一定式英文的
'''