/**
 * Created by pankaicheng on 17/6/29.
 */

$().ready(function(){
    var str = location.href;
    var begin = str.indexOf("=");
    var end = str.length;
    str = str.substr(begin+1,end);
    $.get("/getcontent/?newsid="+str,
        function(result){
            if (result.code == 1){
                $('#newstitle').text(result.body.title);
                $('#news_title').text(result.body.title);
                $('#news-src').text('来源: '+result.body.src);
                $('#news-time').text('时间: '+result.body.time);
                $('#news-content').html(result.body.content.content);
                $('#newsurl').attr('href',result.body.weburl);
            }
        }
    );
    //alert(str);
});