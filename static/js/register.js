/**
 * Created by pankaicheng on 17/6/26.
 */


$().ready(function () {
    //user_valid();
    //alert("open the window");
    $("#register_form").validate({
        submitHandler : function(form) {
            $(form).ajaxSubmit({
                dataType:"json",
                success:function( result ){
                    if( result.code == 1 ){
                       $('#register-modal').modal('hide');

                        alert("注册成功");
                    }else {
                        $('#password1').text("");
                        $('#password2').text("");
                        $('#register_error').text(" * "+ result.msg);
                        alert(result.msg);
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
            },
            repassword: {
                equalTo: "#password1"
            },
            email: {
                required: true,
                email: true
            },
            phone:{
                required : true,
                number: true,
                minlength: 11,
                maxlength: 11
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
            },
            repassword: {
                equalTo: "*两次密码不一样"
            },
            email: {
                required: "*请输入邮箱",
                email: "*请输入有效邮箱"
            },
            phone:{
                required: "*请输入手机号",
                number: '*手机号只能是纯数字',
                minlength: jQuery.validator.format("*请输入正确的手机号"),
                maxlength: jQuery.validator.format("*请输入正确的手机号")
            }
        }

    });

});


$("#close-modal").click(function () {
    $("#login_error").html("");
    $("#login_password").text("");
    $("#bond_id").text("");
    $("#password1").text("");
    $("#password2").text("");
    $("#register_error").html("");
});

