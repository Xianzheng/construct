const myfetch = (url,data) =>{
    const postOptions={
        method:'POST',
            headers:{
                'Content-Type':'application/json',
                'Accept':'Application/json'
            },
            body:JSON.stringify({data})
        }

    var result = fetch(url,postOptions)
            .then(res=>res.json())
    return result
}

const getById = (id) =>  document.getElementById(id)

//conbine js and html
const automatic = () =>{
    console.log('hello world')
    //testLoginPart 在 testConnect.html中
    //login.html 是一小块html代码，这样写为了方便以后复用
    //以后方便读testConnect就直到能理解主逻辑解
    $("#testLoginPart").load("ownWriteHtml/login.html");
    //动态添加的元素，必须以这样的方式添加点击事件

    /*
    *$("#testLoginPart").on('click','#login_submit',function(){})...
    *这个代表动态添加在父级testLoginPart下的所有元素都能被访问
    *但只有id为 login_submit 添加点击事件
    */
    $("#testLoginPart").on('click','#login_submit', function () {
    
        let login_username = $("#login_username").val()
        let login_password = $("#login_password").val()
        loginFetch(login_username,login_password)
            
    });
    
    
}

const loginFetch =(login_username, login_password) => {

    //django backend server(construcor/t4) 
    // python manage.py runserver address is http://127.0.0.1:8000
    // checkIfLogin_api/ is in 
    const url =  'http://127.0.0.1:8000/checkIfLogin_api/'
    
    myfetch(url,{username:login_username,
        password:login_password})
    .then(res => console.log(res))
}


