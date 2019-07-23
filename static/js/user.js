$(function() {
    var cur_user_id = get_page_user_id();
    load_cur_user(cur_user_id);
    search({'user_id': cur_user_id});
});

function load_cur_user(user_id){
    // 获取用户信息
    if(user_id==''){
        alert('用户id不为空');
        return
    }
    $.ajax({
        url: '/user/' + user_id,
        type: 'get',
        dataType: 'json'
    })
    .done(function(user) {
        $('#uimage')[0].src=user.image_url;
        $("#uname").text(user.name);
        $("#udescription").text(user.description);
    })
    .fail(function(err) {
        alert(err.responseText);
    });
}
