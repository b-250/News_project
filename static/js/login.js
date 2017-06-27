/**
 * Created by pankaicheng on 17/4/23.
 */

var is_login = function(){
    $.get("/users/islogin",
        function(result){
            var user_name = result.body.username;
            if (result.code == 1) {
                $("#login-button").hide();
                $("#register-button").hide();
                $("#user-menu").show();
                $("#user-side-menu").text(user_name);
                $("#user-menu-name").text(user_name);
                $("#dropdown-user-name").text(user_name);
            }
            else {
                $("#login-button").show();
                $("#register-button").show();
                $("#user-menu").hide();
                $("#user-side-menu").text("未登录");
            }
        });
};

var add_new = function(id, title, newsurl, img, src, channel, time, abstract){
    var div = $('<div></div>');//document.createElement("div");
    var divid = "news_body"+id;
    div.attr('id',divid);
    div.addClass('box-body');
    //var boxdiv = '<div class="box-body" id = "news_body2"> <div class = "col-md-12 col-xs-12" > <div class="col-md-3 col-xs-5" > <a class="img-wrap" target="_blank" href="/"> <img alt="" src="{% static "images/2.jpg"%}"> </a> </div>  <div class = "col-md-8 col-xs-6" style = "padding-left: 40px"> <div class = "title-box" > <a class = "link-title" target="_blank" href="/"> title </a> </div>         <div>abstract </div> <div class = "extra-box col-md-12 col-xs-12 hidden-xs"> <div class = "col-md-1 col-xs-2 ch-btn">channel </div> <div class = "col-md-3 col-xs-4 src-btn">src </div> <div class = "col-md-4 col-xs-6 time-btn">time </div> </div> </div> </div> </div><hr/>';


    //div.addClass('box');
    //div.addClass('box-default');
    var imgname = img;
    var imgdiv_ = '<div class="col-md-3 col-xs-5" > <a class="img-wrap" target="_blank" href="'+ newsurl + '"> <img alt="" src='+ imgname +'>'+ '</a> </div>';
    var imgdiv = $(imgdiv_);
    var textdiv = $(' <div class = "col-md-offset-1 col-xs-offset-1 col-md-8 col-xs-6" style = "padding-left: 40px"></div>');
    var titlediv = $('<div class = "title-box" > <a class = "link-title" target="_blank" href="/">'+ title +'</a> </div>');
    var absdiv = $('<div>'+abstract+'</div>');
    var chdiv = $('<div class = "col-md-2 col-xs-3 ch-btn">'+channel+'</div>');
    var srcdiv = $('<div class = "col-md-3 col-xs-3 src-btn">来源:'+src+'</div>');
    var timediv = $('<div class = "col-md-3 col-xs-5 time-btn">'+time+'</div>');
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

    $("#load-button").after(div);
    //div.after('<hr/>');
    $("#load-button").remove();
    div.after('<hr/><div id="load-button"></div>');

};

var load_new = function(num){

    for(var i=0; i<num; i++)
    {
        add_new(i,'test_news','/','/static/images/2.jpg','新浪','新闻','2017-6-28','this is news abstract');
    }
};


$().ready(function () {
    $("#user-menu").hide();
    is_login();
    load_new(10);
    $("#login_form").validate({
        submitHandler : function (form) {
            //alert("post");
            var log_type = $("input[name='loginType']:checked").val();
            $(form).ajaxSubmit({
                dataTypes: "json",
                success: function (result) {
                    if (result.code == 1) {
                        alert(result.msg);
                        var user_name = result.body.username;
                        window.location.href = "/";
                        $('#login-modal').modal('hide');
                        $("#login-button").hide();
                        $("#register-button").hide();
                        $("#user-menu").show();
                        $("#user-side-menu").text(user_name);
                        $("#user-menu-name").text(user_name);
                        $("#dropdown-user-name").text(user_name);
                    }
                    else if (result.code == 0) {
                        $("#user-menu").hide();
                        alert(result.msg);
                        $("#login_password").text("");
                    }
                }
            });
        },
        rules: {
            username: {
                required: true,
                minlength: 5,
                maxlength: 20
            },
            password: {
                required: true,
                minlength: 6,
                maxlength: 20
            }
        },
        messages: {
            username: {
                required: "*请输入用户名",
                minlength: jQuery.validator.format("*用户名不能小于{0}个字符"),
                maxlength: jQuery.validator.format("*用户名不能大于{0}个字符"),
                notnumber: "*用户名不能是纯数字"
            },
            password: {
                required: "*请输入密码",
                minlength: jQuery.validator.format("*密码不能小于{0}个字符"),
                maxlength: jQuery.validator.format("*密码不能大于{0}个字符")
            }
        }

    });
});

$('#jumptoregister').click(function(){
    $('#login-modal').modal('hide');
    $('#register-modal').modal('show');
});

$('#jumptologin').click(function(){
    $('#login-modal').modal('show');
    $('#register-modal').modal('hide');
});

$('#logout').click(function(){
    //alert("logout");
    $.get("users/logout",
        function(result){
            if (result.code==0) {
                alert("登出成功");
                window.location.href = "/";
                $("#login-button").show();
                $("#register-button").show();
                $("#user-menu").hide();
                $("#user-side-menu").text("未登录");
            }
        });
});
