$(function() {
    is_user(); //判断用户是否登陆，未登陆先跳转到登录页
    md_load(); //加载Markdown插件

});

function is_user(){
    var uname = String(window.localStorage.uname);
    if(uname == "undefined"){
        window.location.replace("login.html");
    }
}

function md_load(){
    editormd("my-editormd", { //注意1：这里的就是上面的DIV的id属性值
        width: "80%",
        height: 640,
        toolbar: true,
        toolbarIcons: function() {
            return ["undo", "redo", "|", "bold", "hr", "|", "h1", "code", "reference", "||", "watch", "fullscreen", "preview", "saveIcon", "info"]
        },
        // previewTheme : "3024-day",
        editorTheme: "3024-day",
        syncScrolling: "single",
        path: "lib/", //注意2：你的路径
        saveHTMLToTextarea: true, //注意3：这个配置，方便post提交表单
        toolbarIconTexts: {
            saveIcon: "上传" // 如果没有图标，则可以这样直接插入内容，可以是字符串或HTML标签
        },
        toolbarHandlers: {
            saveIcon: function(cm, icon, cursor, selection) {
                send();
            }
        },
    });
}

function send(){
    var title = $("#title").val().trim();
    if (title == ""){
        alert("标题不能为空");
        return
    }

    var data = {
        "title": title,
        "content": $('#my-editormd-markdown-doc').val().trim()
    };
    $.ajax({
        url: '/article',
        type: 'post',
        data: data
    })
    .done(function(data) {
        alert('提交成功');
        console.log(data);
    })
    .fail(function(err) {
        alert(err.responseText);
    })
}
