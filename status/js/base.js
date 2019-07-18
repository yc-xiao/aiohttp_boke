$(function() {
    $('header').first().load("../base.html");
    timeId = setTimeout(main, 10);

});
function main(){
    dlbox_func();
    $("#login-back").on('click', onback);
    console.log($("#login-back"));
}

function dlbox_func(){
    var inputs = $(".dlbox a");
    var uname = String(window.localStorage.uname);
    if (uname != 'undefined') {
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

function onback(){
    $.ajax({
        url: '/api/back',
        type: 'post',
    })
    .done(function() {
        console.log(22)
        window.localStorage.uname = "undefined";
    })

}
