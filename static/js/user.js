$(function() {
    var cur_user_id = get_page_user_id();
    load_cur_user(cur_user_id);
    search({'user_id': cur_user_id});
});

function load_cur_user(user_id){
    // 获取用户信息
    console.log(user_id);
    $.ajax({
        url: '/user/' + user_id,
        type: 'get',
        dataType: 'json'
    })
    .done(function(user) {
        console.log(user);
        user.tell = "这是小明，他喜欢打游戏";
        $('#uimage')[0].src=user.image_url;
        $("#uname").text(user.name);
        $("#udescription").text(user.description);
    })
    .fail(function(err) {
        alert(err.responseText);
    });
}

// function get_user_id(){
//     var uname = String(window.localStorage.uname);
//     if(uname == "undefined" || uname == ""){
//         window.location.replace("login.html");
//     }
//     var token = cookie_to_obj()['token'];
//     if(typeof token == "undefined"){
//         window.location.replace("login.html");
//     }
//     user_id = token.split("_")[0];
//     return user_id
// }
//
// function cookie_to_obj(){
//     var obj = {};
//     var cookie = document.cookie;
//     var cookies = cookie.split(";");
//     for(let i=0; i<cookies.length; i++){
//         let temp = cookies[i].split("=");
//         obj[temp[0]] = temp[1];
//     }
//     return obj
// }
