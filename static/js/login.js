/**
 * Created by pankaicheng on 17/4/23.
 */

$().ready(function () {
    $("#user-menu").hide();
    $("#login_form").validate({
        submitHandler : function (form) {
            //alert("post");
            var log_type = $("input[name='loginType']:checked").val();
            $(form).ajaxSubmit({
                dataTypes: "json",
                success: function (result) {
                    //alert(result.code);
                    if (result.code == 0) {
                        $("#user-menu").hide();
                        alert(result.msg);
                        $("#login_password").text("");
                    }
                    else if (result.code == 1 || result.code == 2) {
                        alert(result.msg);
                        //window.location.href = "/";
                        $('#login-modal').modal('hide');
                        $("#login-button").hide();
                        $("#register-button").hide();
                        $("#user-menu").show();
                        $("#usermenu").text(result.userinfo.username);
                        $("#user-menu-name").text(result.userinfo.username);
                        $("#dropdown-user-name").text(result.userinfo.username);
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