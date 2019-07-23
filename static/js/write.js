$(function() {
    md_data = is_cur_user(); //判断用户
    md_load(md_data); //加载Markdown插件
});

function is_cur_user(){
    /*
        1.如果是write.html页面说明是用户要新增文章，则判断用户是否登陆
        2.如果是/a/article_id页面说明是访问文章，如果用户是当前文章的作者则可以修改文章，其他只允许查看。
    */
    var md_data = {
        'article': {},
        'is_writor':false,
    };
    var path = window.location.pathname;
    if(path == '/write.html'){
        var uname = String(window.localStorage.uname);
        if(uname == "undefined" || uname == ""){
            window.location.replace("login.html");
        }
        md_data.is_writor = true;
    }
    else{
        var article_id = path.replace('/a/','');
        var article = get_ariticle(article_id);
        md_data.article = article;
        if(localStorage.uuser_id == article.writor_id){
            md_data.is_writor = true;
        }
    }
    return md_data
}


function md_load(md_data){
    if(md_data.article != {}){
        $('#title').first().attr('value',md_data.article.title);
        $('#description').first().attr('value',md_data.article.description);
        $('#my-editormd-markdown-doc').first().text(md_data.article.content);
    }
    if(md_data.is_writor){
        $('#title').first().attr('readOnly', false);
        $('#description').first().attr('readOnly', false);
        if(window.location.pathname != '/write.html'){
            $('#ebox').append('<input type="button" name="update" id="update" value="更新"><input type="button" name="delete" id="delete" value="丢弃">');
            $("#update").on('click', update);
            $("#delete").on('click', delete_func);
        }
        markdown_html();

    }
    else{
        $('#title').first().attr('readOnly', true);
        $('#description').first().attr('readOnly', true);
        markdown2html();
    }

}

function send(){
    var title = $("#title").val().trim();
    if (title == ""){
        alert("标题不能为空");
        return
    }

    var data = {
        "title": title,
        "description": $('#description').val().trim(),
        "content": $('#my-editormd-markdown-doc').val().trim(),
        "writor": window.localStorage.uname
    };
    $.ajax({
        url: '/article',
        type: 'post',
        data: data
    })
    .done(function(data) {
        alert('提交成功');
        window.location.replace("index.html");
    })
    .fail(function(err) {
        alert(err.responseText);
    })
}

function get_ariticle(article_id){
    var article;
    if(article_id.length != 32){
        window.location.replace("index.html");
    }
    $.ajax({
        url: '/article/' + article_id,
        type: 'get',
        dataType: 'json',
        async: false
    })
    .done(function(data) {
        article = data
        console.log("success");
    })
    .fail(function(res) {
        console.log("error");
        window.location.replace("index.html");
    });
    return article
}

function update(){
    var title = $("#title").val().trim();
    var path = window.location.pathname;
    var article_id = path.replace('/a/','');
    if (title == ""){
        alert("标题不能为空");
        return
    }
    if(article_id.length != 32){
        alert("文章id错误!");
        return
    }
    var data = {
        "title": title,
        "article_id": article_id,
        "user_id": localStorage.uuser_id,
        "description": $('#description').val().trim(),
        "content": $('#my-editormd-markdown-doc').val().trim()
    }

    $.ajax({
        url: '/article',
        type: 'put',
        data: data
    })
    .done(function(data) {
        alert('文章更新成功!');
        console.log("success");
    })
    .fail(function(res) {
        console.log(res.responseText);
    });
}
function delete_func(){
    var path = window.location.pathname;
    var article_id = path.replace('/a/','');
    if(article_id.length != 32){
        alert('文章id错误!');
        return
    }
    $.ajax({
        url: '/article/' + article_id,
        type: 'delete',
    })
    .done(function(data) {
        window.location.replace("/user.html");
    })
    .fail(function(res) {
        console.log(res.responseText);
    });
}

function markdown2html(){
    $('#my-editormd').first().css('margin', 'auto').css('width','60%');
    editormd.markdownToHTML("my-editormd", {
        htmlDecode: "style,script,iframe"
    });
}

function markdown_html(){
    editormd("my-editormd", { //注意1：这里的就是上面的DIV的id属性值
        width: "80%",
        height: 640,
        toolbar: true,
        toolbarIcons: function() {
            return ["undo", "redo", "|", "bold", "hr", "|", "h1", "code", "reference", "||", "watch", "fullscreen", "preview", "saveIcon", "info"]
        },
        readOnly: !md_data.is_writor,
        watch: false,
        // previewTheme : "3024-day",
        editorTheme: "3024-day",
        syncScrolling: "single",
        path: "/static/lib/", //注意2：你的路径
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
