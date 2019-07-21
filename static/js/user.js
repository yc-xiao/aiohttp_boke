$(function() {
    var user_id = get_user_id(); //判断用户是否登陆，未登陆先跳转到登录页
    data = {
        'index':0,
        'nums':10,
        'user_id':user_id,
        'title':'a1'
    }
    load_cur_user(user_id=user_id);
    load_ariticle(data);
});

function get_user_id(){
    var uname = String(window.localStorage.uname);
    if(uname == "undefined"){
        window.location.replace("login.html");
    }
    var token = cookie_to_obj()['token'];
    if(typeof token == "undefined"){
        window.location.replace("login.html");
    }
    user_id = token.split("-")[0];
    return user_id
}

function cookie_to_obj(){
    var obj = {};
    var cookie = document.cookie;
    var cookies = cookie.split(";");
    for(let i=0; i<cookies.length; i++){
        let temp = cookies[i].split("=");
        obj[temp[0]] = temp[1];
    }
    return obj
}


function load_cur_user(user_id=user_id){
    // 获取用户信息
    $.ajax({
        url: '/user/' + user_id,
        type: 'get',
        dataType: 'json'
    })
    .done(function(data) {
        let user = data;
        user.src = "uimages/ddm.jpg";
        user.tell = "这是小明，他喜欢打游戏";
        $('#uimage')[0].src=user.src;
        $("#uname").text(user.name);
        $("#utell").text(user.tell);
    })
    .fail(function(err) {
        alert(err.responseText);
    });
}

function load_ariticle(data){
    // 获取文章
    $.ajax({
        url: '/api/articles',
        type: 'post',
        dataType: 'json',
        data: data
    })
    .done(function() {
        console.log("success");
    })
    .fail(function() {
        console.log("error");
    });
}
