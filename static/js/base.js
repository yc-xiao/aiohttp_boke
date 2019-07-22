$(function() {
    $('header').first().load("../base.html");
    timeId = setTimeout(main, 10);
    get_user();
});

function main(){
    dlbox_func();
    $("#login-back").on('click', onback);
    $("#user-home").on('click', onhome);
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
}
function get_user(){
    $.ajax({
        url: '/api/is_login',
        type: 'post',
        dataType: 'json',
        data: {}
    })
    .done(function(data) {
        window.localStorage.user = data;
        window.localStorage.uname = data['name'];
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
        window.localStorage.user = {};
        window.localStorage.uname = '';
    })
}
function onhome(){
    $.ajax({
        url: '/api/back',
        type: 'post',
    })
    .done(function() {
        window.localStorage.uname = "undefined";
    })
}
