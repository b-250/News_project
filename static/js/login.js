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
                $("#user-side-menu").html(user_name);
                $("#user-menu-name").text(user_name);
                $("#dropdown-user-name").text(user_name);
                $("#inoff").text('Online');
            }
            else {
                $("#login-button").show();
                $("#register-button").show();
                $("#user-menu").hide();
                $("#user-side-menu").html("未登录");
                $("#inoff").text('Offline');
            }
        });
};

$().ready(function () {
    $("#user-menu").hide();
    is_login();


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
                        $("#user-side-menu").html(user_name);
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
                $("#user-side-menu").html("未登录");
            }
        });
});
