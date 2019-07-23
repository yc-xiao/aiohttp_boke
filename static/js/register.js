$(function(){
    var uname = String(window.localStorage.uname);
    if(uname != "undefined" || uname == ""){
        window.location.replace("/index.html");
    }
})

//注册点击事件
$('#register').click(function(event) {
    var flag = 0;
    var inputs = $(".dbox input");
    inputs.each(function(index, el) {
        if(index==0){
            flag = (el.value.length >= 2) ? flag:1;
        }
        if(index<3 && index >0){
            flag = (el.value.length >= 8) ? flag:2;
        }
    });
    if (inputs[1].value != inputs[2].value){
        flag = 3;
    }
    switch(flag){
        case 0:
            send({name:inputs[0].value,password:inputs[1].value});
            break;
        case 1:
            alert("账号长度最小为2");break;
        case 2:
            alert("密码长度最小为8");break;
        case 3:
            alert("密码不相同");break;
    }
});

//注册函数
function send(data){
    $.ajax({
        url: '/user/',
        type: 'post',
        data: data,
        // 根据接口返回数据设置，若返回结果跟数据格式不一致，不会调用success函数
        // dataType: 'json',
        success: function (data) {
            var timeId = setTimeout(function(){
                window.location.replace("/login.html");
            },500);
        },
        error: function (err) {
            alert(err.responseText);
        }
    })
};
