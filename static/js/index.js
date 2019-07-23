$(document).ready(function() {
    // get_articles();
    search({});
});
// function get_articles(){
//     $.ajax({
//         url: '/api/articles',
//         type: 'post',
//         dataType: 'json',
//         data: {}
//     })
//     .done(function(articles) {
//         let dbox = $('#boxs');
//         for(let key in articles){
//
//             let  text = "<div class='abox'>\
//                 <h3><a href=''>%title%</a></h3><p>%description%</p>\
//                 <div>\
//                     <span>作者:</span>\
//                     <span>%writor%</span>&nbsp&nbsp&nbsp&nbsp\
//                     <span>时间:</span>\
//                     <span>%created%</span>\
//                 </div>\
//             </div>";
//             let art = articles[key];
//             art['created'] = get_local_time(art['created']);
//             for(let e in art){
//                 let temp = "%" + String(e) + "%";
//                 text = text.replace(temp, art[e]);
//             }
//             dbox.append(text);
//         }
//         console.log(articles);
//     })
//     .fail(function(err) {
//         alert(err.responseText);
//     });
// }
// function get_local_time(time){
//     time = parseInt(time) * 1000;
//     var date = new Date(time);
//     return date.toLocaleDateString()
// }
