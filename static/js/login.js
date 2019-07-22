$(function(){
    $("#logon-submit").on('click', onlogin);
    var uname = String(window.localStorage.uname);
    if(uname != "undefined" || uname == ""){
        window.location.replace("index.html");
    }
})
//点击事件
function onlogin(event) {
    console.log('helloc');
    var name = $("#login-name").val().trim();
    var password = $("#login-password").val().trim()
    if(name == "" || password == ""){
        alert("账号和密码不能为空");
    }
    else{
        data = {"name":name, "password":password};
        send(data);
    }
}

// 登陆函数
function send(data){
    $.ajax({
        url: '/api/login',
        type: 'post',
        data: data,
        // dataType: 'json',
        success: function (data) {
            window.localStorage.uname = data.name;
            window.location.replace("index.html");
        },
        error: function (err) {
            alert(err.responseText);
        }
    })
};
