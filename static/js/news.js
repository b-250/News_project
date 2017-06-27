/**
 * Created by pankaicheng on 17/6/28.
 */

var add_new = function(id, title, newsurl, img, src, channel, time, abstract){
    var div = $('<div></div>');//document.createElement("div");
    var divid = "news_body"+id;
    div.attr('id',divid);
    div.addClass('box-body');
    //var boxdiv = '<div class="box-body" id = "news_body2"> <div class = "col-md-12 col-xs-12" > <div class="col-md-3 col-xs-5" > <a class="img-wrap" target="_blank" href="/"> <img alt="" src="{% static "images/2.jpg"%}"> </a> </div>  <div class = "col-md-8 col-xs-6" style = "padding-left: 40px"> <div class = "title-box" > <a class = "link-title" target="_blank" href="/"> title </a> </div>         <div>abstract </div> <div class = "extra-box col-md-12 col-xs-12 hidden-xs"> <div class = "col-md-1 col-xs-2 ch-btn">channel </div> <div class = "col-md-3 col-xs-4 src-btn">src </div> <div class = "col-md-4 col-xs-6 time-btn">time </div> </div> </div> </div> </div><hr/>';

    //div.addClass('box');
    //div.addClass('box-default');
    var imgname;
    if(img!="")
        imgname = img;
    else
        imgname = "static/images/2.jpg";
    var imgdiv_ = '<div class="col-md-3 col-xs-5" > <a class="img-wrap" target="_blank" href="'+ newsurl + '"> <img alt="" src='+ imgname +'>'+ '</a> </div>';
    var imgdiv = $(imgdiv_);
    var textdiv = $(' <div class = "col-md-offset-1 col-xs-offset-1 col-md-8 col-xs-6" style = "padding-left: 40px"></div>');
    var titlediv = $('<div class = "title-box" > <a class = "link-title" target="_blank" href="'+ newsurl+'">'+ title +'</a> </div>');
    var absdiv = $('<div>'+' '+'</div>');
    var chdiv = $('<div class = "col-md-1 col-xs-2 ch-btn">'+channel+'</div>');
    if(src=='')
        src = "新浪网";
    var srcdiv = $('<div class = "col-md-4 col-xs-4 src-btn">来源:'+src+'</div>');
    if(time=='')
        time = '刚刚';
    var timediv = $('<div class = "col-md-5 col-xs-6 time-btn">时间:'+time+'</div>');
    var footdiv = $('<div class = "extra-box col-md-12 col-xs-12 hidden-xs"></div>');
    var boxdiv = $('<div class = "col-md-12 col-xs-12" ></div>');
    footdiv.append(chdiv);
    footdiv.append(srcdiv);
    footdiv.append(timediv);
    textdiv.append(titlediv);
    textdiv.append(absdiv);
    textdiv.append(footdiv);
    boxdiv.append(imgdiv);
    boxdiv.append(textdiv);
    div.append(boxdiv);
    //div.append('<div class = "col-md-12 col-xs-12" >   </div>');

    $("#load-buttom").after(div);
    //div.after('<hr/>');
    $("#load-buttom").remove();
    div.after('<hr/><div id="load-buttom"></div>');

};

var load_new = function(num,channel,channelname){
    var news_list;
    $.post("/getnews",
        {
            channel: channel
        },
        function(result){
            if (result.code == 1){
                news_list = result.body;
                //alert(news_list.length);
                //alert(news_list[1].src);
                for(var i=0; i<num; i++)
                {
                    add_new(i,news_list[i].title,news_list[i].weburl,news_list[i].pic,news_list[i].src,channelname,news_list[i].time,'this is news abstract');
                }
            }
        }
    );
};

$().ready(function () {

    load_new(10,'new','新闻');

});

$("#new-news").click(function(){
    var activeli =$("ul li.active");
    activeli.attr("class","");
    $("#new-news").attr("class","active");
    load_new(10,'new');
});



