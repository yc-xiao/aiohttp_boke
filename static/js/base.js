$(function() {
    $('header').first().load("../base.html");
    timeId = setTimeout(main, 10);
});

function main(){
    get_user(); // 判断用户是否登陆
    dlbox_func(); // 根据用户状态，修改导航栏
    // 导航栏按钮添加点击事件
    $("#login-back").on('click', onback);
    $("#search-button").on('click', psearch);
}

function dlbox_func(){
    var inputs = $(".dlbox a");
    var uname = String(window.localStorage.uname);
    if (uname != 'undefined' || uname == '') {
        var block2 = 'inline-block';
        var block1 = 'none';
        inputs.eq(2).text(uname);
    }
    else{
        var block1 = 'inline-block';
        var block2 = 'none';
        inputs.eq(2).text("");
    }
    inputs.eq(0).css('display', block1);
    inputs.eq(1).css('display', block1);
    inputs.eq(2).css('display', block2);
    inputs.eq(3).css('display', block2);
    inputs.eq(4).css('display', block2);

    var path = window.location.pathname;
    if(path.match('(/u/)|user.html|index.html')){
        $('#ssbox').css('display', 'inline');
    }else{
        $('#ssbox').css('display', 'none');
    }
}

function get_user(){
    $.ajax({
        url: '/api/is_login',
        type: 'post',
        dataType: 'json',
        data: {}
    })
    .done(function(data) {
        window.localStorage.uname = data['name'];
        window.localStorage.uuser_id = data['user_id']
    })
    .fail(function() {
        console.log("error");
    })
}

function onback(){
    $.ajax({
        url: '/api/back',
        type: 'post',
    })
    .done(function() {
        document.cookie = "token=''";
        window.localStorage.uname = '';
        window.localStorage.uuser_id = '';
        window.location.replace("/index.html");
    })
}

function psearch(){
    var title = $('#search-key').val().trim();
    data = {
        'title': title,
        'user_id': get_page_user_id(),
        'nums': 10,
        'index': 0
    }
    search(data);
}

function search(data){
    $.ajax({
        url: '/api/articles',
        type: 'post',
        data: data
    })
    .done(function(articles) {
        let dbox = $('#boxs');
        dbox.empty();
        for(let key in articles){
            let  text = "<div class='abox'>\
                <h3><a href='%title_url%' >%title%</a></h3><p>%description%</p>\
                <div>\
                    <span>作者:&nbsp&nbsp</span>\
                    <a href='%writor_url%'>%writor%</a>&nbsp&nbsp&nbsp&nbsp\
                    <span>时间:</span>\
                    <span>%created%</span>\
                </div>\
            </div>";
            let art = articles[key];
            art['created'] = get_local_time(art['created']);
            art['title_url'] = '/a/' + art['article_id'];
            art['writor_url'] = '/u/' + art['writor_id'];
            for(let e in art){
                let temp = "%" + String(e) + "%";
                text = text.replace(temp, art[e]);
            }
            dbox.append(text);
        }
    })
}


function get_page_user_id(){
    var user_id = '';
    var path = window.location.pathname;
    if(path == '/user.html'){
        var uuser_id = window.localStorage.uuser_id;
        if(uuser_id && uuser_id != 'undefined'){
            user_id = uuser_id;
        }
    }
    else{
        var path = path.replace('/u/','');
        if(path.length == 32){
            user_id = path;
        }
    }
    return user_id
}
function get_local_time(time){
    time = parseInt(time) * 1000;
    var date = new Date(time);
    return date.toLocaleDateString()
}
