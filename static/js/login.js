/**
 * Created by pankaicheng on 17/4/23.
 */

$().ready(function () {

    $("#login_form").validate({
        submitHandler : function () {
            var log_type = $("input[name='loginType']:checked").val();
            $.post("/users/login",
                {
                    username: $('#login_bond_id').val(),
                    password: $('#login_password').val(),
                },
                function (result) {

                    if (result.code==1){
                        $("#user-menu").hide();
                        alert("用户名或密码错误");
                    }
                    else if (result.code ==0){
                        alert("登录成功");
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
            )
        },
        rules: {
            username: {
                required: true,
                minlength: 6,
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