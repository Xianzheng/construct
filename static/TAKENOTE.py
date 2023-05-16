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
bootstrap id 找不到,可以用className,然后.id

<script>
    let ele = document.getElementsByClassName('navbar navbar-light').navbar_content
    let url = window.location.href
    let lst = url.split('/')
    let appName = lst[3]
    console.log(appName)
    let arrayText = [['总表','table1'],['视觉化1','visual1'],['视觉化1','visual2']] 
    arrayText.forEach(element => {
        let addTag = document.createElement('a')
        addTag.innerHTML = element[0]
        addTag.setAttribute('href','/'+appName+'/'+element[1]+'/')
        ele.append(addTag)
    })
    let addTag1 = document.createElement('a')
    addTag1.innerHTML = '构建'
    addTag1.setAttribute('href','/app/addApp/')
    ele.append(addTag1)
    let addTag2 = document.createElement('a')
    addTag2.innerHTML = '登出'
    addTag2.setAttribute('href','/logout/')
    ele.append(addTag2)
</script>
'''

'''

echarts和djangoView 配合：

在views中return 必须是{"msg":json.dumps({"msg":data})}

在template的script才能收到
var dataName = {{msg|safe}}

echars 中 legends数据必须和series 的 name一样才能显示
legend: {data:[dataName.name]},
series: [{name: dataName.name,type: 'bar',data: yRes}]
'''

'''
url中
 path('visual/<tableId>',visual_view),
view中
def visual(request,tableId):
    pass

tableId应该不算参数


<script>
    function V1_jumpTo(name){
      console.log('hello jump to',name)
      fetch('/武汉分公司气耗/visual1/',{
      method:"POST",
      body:JSON.stringify({'name':name})
    }).then(res => res.json())
      .then(res => {
        //alert('更新成功')
        window.location.href = "http://127.0.0.1:8000/%E6%AD%A6%E6%B1%89%E5%88%86%E5%85%AC%E5%8F%B8%E6%B0%94%E8%80%97/visual1?name="+res.name
      })
    }
  </script>


前端页面发起fetch请求传递参数

url path('visual/',visual_view),

127.0.0.1/visual 和 127.0.0.1/visual?name=mark

会到同一个visual_visual所以可以对parameter做一些处理

url -> view ->html,如果有fetch可以改变流程
'''

'''

给ul添加滚动条， 直接在 ul上添加style=“height:800px;overflow-y:scroll;”

 const selectClick2 = async () => {

       await fetch('/app/getUploadFiles/', {
          method: "GET",
        })
}

async，await可以把同步转异步

動態引用庫方法
import importlib
# table1 = importlib.import_module('.models', package=appName)
module=importlib.import_module(appName+".models")
add = module.table1

#请求乱码转中文
urllib.parse.unquote(app_name)


request.get_full_path()

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <!--
          为了让 Bootstrap 开发的网站F对移动设备友好，确保适当的绘制和触屏缩放，
          需要在网页的 head 之中添加 viewport meta 标签,一般将bootstrap的css和js文件放进来的时候会自动生成
          -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0,shrink-to-fit=no">
        <!--width=device-width 表示宽度是设备屏幕的宽度。
              initial-scale=1.0 表示初始的缩放比例。
              shrink-to-fit=no 自动适应手机屏幕的宽度。这里的shrink-to-fit=no"是我自己加进去的-->
        <title>bootstrap测试</title>
      
        <link href="./bootstrap/css/bootstrap.css" type="text/css" rel="stylesheet">
</head>
<body>
    <div id="popover1" class="col-sm-12 col-xs-12 col-md-9">
        <div><a href ="#"class="change-trigger" title="" >Popover Example</a></div>

        <div id="select-div" class="hide" style="display: none;">
            <div><a href="#">使用时长</a></div>
            <div><a href="#">维修情况</a></div>
            <div><a href="#">维修情况</a></div>
        </div>
    </div>
    <script src="./js_lib/jquery-3.6.4.min.js"></script>
    <script src="./bootstrap/js/bootstrap.bundle.min.js"></script> 
    <script src="./js_lib/popper.min.js"></script>
    <script src="./bootstrap/js/bootstrap.js"></script>
    <script>
    $('.change-trigger').popover({
        placement : 'Right',
        // title : 'Change',
        trigger : 'manual',
        html : true,
        content : function(){
            var content = '';
            content = $('#select-div').html();
            return content;
        } 
    }).on("mouseenter", function() {
		// console.log($(".hx-flot_window li a").css)
		var _this = this; // 这里的this触发的dom,需要存起来 否则在下面 .popover的逻辑中this会变为弹出的dom
		$(this).popover("show");
		$(".popover").on("mouseleave", function() {
			$(_this).popover('hide');
		});
	}).on("mouseleave", function() {
		var _this = this;
		setTimeout(function() {
			if (!$(".popover:hover").length) {
				$(_this).popover("hide");
			}
		}, 100);
	});
    
    </script>
</body>
</html>


'''