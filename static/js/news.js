/**
 * Created by pankaicheng on 17/6/28.
 */

var add_new = function(id, title, newsurl, img, src, channel, time, newsid){
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
    var myurl = "/newscontent/?newsid="+newsid;
    var imgdiv_ = '<div class="col-md-3 col-xs-5" > <a target="_blank" href="'+ myurl + '"> <img class="img-responsive" alt="" src='+ imgname +'>'+ '</a> </div>';
    var imgdiv = $(imgdiv_);
    var textdiv = $(' <div class = "col-md-offset-1 col-md-8 col-xs-7"></div>');
    var titlediv = $('<div class = "title-box col-md-10 col-xs-12" > <a class = "link-title" target="_blank" href="'+ myurl+'">'+ title +'</a> </div>');
    var absdiv = $('<div>'+' '+'</div>');
    var chdiv = $('<div class = "col-md-3 col-xs-3">分类:'+channel+'</div>');
    if(src=='')
        src = "新浪网";
    var srcdiv = $('<div class = "col-md- col-xs-3">来源:'+src+'</div>');
    if(time=='')
        time = '刚刚';
    var timediv = $('<div class = "col-md-5 col-xs-5">时间:'+time+'</div>');
    var footdiv = $('<div class = "col-md-11 col-xs-11 hidden-xs"></div>');
    var boxdiv = $('<div class = "col-md-12 col-xs-12" ></div>');
    footdiv.append(chdiv);
    footdiv.append(srcdiv);
    footdiv.append(timediv);
    textdiv.append(titlediv);
    textdiv.append('<div class="col-md-10 col-xs-10"><br/></div>');
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

var cnt = 0;
var opts = {
    lines: 13, // 花瓣数目
    length: 9, // 花瓣长度
    width: 5, // 花瓣宽度
    radius: 9, // 花瓣距中心半径
    corners: 1, // 花瓣圆滑度 (0-1)
    rotate: 0, // 花瓣旋转角度
    direction: 1, // 花瓣旋转方向 1: 顺时针, -1: 逆时针
    color: '#5882FA', // 花瓣颜色
    speed: 1, // 花瓣旋转速度
    trail: 60, // 花瓣旋转时的拖影(百分比)
    shadow: false, // 花瓣是否显示阴影
    hwaccel: false, //spinner 是否启用硬件加速及高速旋转
    className: 'spinner', // spinner css 样式名称
    zIndex: 2e9, // spinner的z轴 (默认是2000000000)
    top: 'auto', // spinner 相对父容器Top定位 单位 px
    left: window.innerWidth/3// spinner 相对父容器Left定位 单位 px
};
var spinner = new Spinner(opts);

var clear_news = function(){
    for(var i=0; i<cnt; i++){
        var divid = "news_body" + i;
        //alert(divid);
        var div = document.getElementById(divid);
        div.remove();
    }
    var hr = $('hr');
    hr.remove();
    cnt = 0;
};

var load_new = function(num,channel,channelname){
    var news_list;
    var target = $("#load-buttom").get(0);
    spinner.spin(target);
    $.post("/getnews",
        {
            channel: channel,
            num : num,
            begin : cnt
        },
        function(result){
            if (result.code == 1){
                news_list = result.body;
                //alert(news_list.length);
                //alert(news_list[1].src);
                for(var i=0; i<news_list.length; i++)
                {
                    add_new(i+cnt,news_list[i].title,news_list[i].weburl,news_list[i].pic,news_list[i].src,channelname,news_list[i].time,news_list[i].id);
                }
                cnt +=news_list.length;
            }
        }
    );
    // 关闭spin
    spinner.spin();
};

$().ready(function () {

    load_new(10,'rec','头条');

});

var thischannel = 'rec';
var thischannelname = '头条';
$("#new-recommend").click(function(){
    var activeli =$("ul li.active");
    activeli.attr("class","");
    $("#new-recommend").attr("class","active");
    clear_news();
    load_new(10,'rec',"头条");
    thischannel = 'rec';
    thischannelname = '头条';
    cnt = 0;
});

$("#news-news").click(function(){
    var activeli =$("ul li.active");
    activeli.attr("class","");
    $("#news-news").attr("class","active");
    clear_news();
    load_new(10,'news',"新闻");
    thischannel = 'news';
    thischannelname = '新闻';
    cnt = 0;
});

$("#finance-news").click(function(){
    var activeli =$("ul li.active");
    activeli.attr("class","");
    $("#finance-news").attr("class","active");
    clear_news();
    load_new(10,'finance',"财经");
    thischannel = 'finance';
    thischannelname = '财经';
    cnt = 0;
});

$("#sports-news").click(function(){
    var activeli =$("ul li.active");
    activeli.attr("class","");
    $("#sports-news").attr("class","active");
    clear_news();
    load_new(10,'sports',"体育");
    thischannel = 'sports';
    thischannelname = '体育';
    cnt =0;
});

$("#ent-news").click(function(){
    var activeli =$("ul li.active");
    activeli.attr("class","");
    $("#ent-news").attr("class","active");
    clear_news();
    load_new(10,'ent',"娱乐");
    thischannel = 'ent';
    thischannelname = '娱乐';
    cnt = 0;
});

$("#mil-news").click(function(){
    var activeli =$("ul li.active");
    activeli.attr("class","");
    $("#mil-news").attr("class","active");
    clear_news();
    load_new(10,'mil',"军事");
    thischannel = 'mil';
    thischannelname = '军事';
    cnt =0 ;
});

$("#edu-news").click(function(){
    var activeli =$("ul li.active");
    activeli.attr("class","");
    $("#edu-news").attr("class","active");
    clear_news();
    load_new(10,'edu',"教育");
    thischannel = 'edu';
    thischannelname = '教育';
    cnt = 0;
});

$("#tech-news").click(function(){
    var activeli =$("ul li.active");
    activeli.attr("class","");
    $("#tech-news").attr("class","active");
    clear_news();
    load_new(10,'tech',"科技");
    thischannel = 'tech';
    thischannelname = '科技';
    cnt = 0;
});

$("#nba-news").click(function(){
    var activeli =$("ul li.active");
    activeli.attr("class","");
    $("#nba-news").attr("class","active");
    clear_news();
    load_new(10,'nba',"NBA");
    thischannel = 'nba';
    thischannelname = 'NBA';
    cnt = 0;
});

$("#stock-news").click(function(){
    var activeli =$("ul li.active");
    activeli.attr("class","");
    $("#stock-news").attr("class","active");
    clear_news();
    load_new(10,'stock',"股票");
    thischannel = 'stock';
    thischannelname = '股票';
    cnt = 0;
});


$(window).scroll(function(){
    /*if (getScrollTop()+ getClientHeight()>flagPos){
        alert(getScrollTop());
        alert(flagPos);
        alert(getClientHeight());
    }*/
    var top = document.documentElement.scrollTop || document.body.scrollTop;
    var height = document.documentElement.scrollHeight || document.body.scrollHeight;
    var winH = window.innerHeight || document.documentElement.clientHeight||document.body.clientHeight;
    if (top+winH >= height){
        //alert('at buttom');
        load_new(10,thischannel,thischannelname);
    }
});

