# encoding: utf-8
from django.shortcuts import render
from users.models import MyUser
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import authenticate
# Create your views here.
from newsbackend.common import respond_assemble

def show_login(request):
    return render(request, 'login.html')

@require_POST
@csrf_exempt
def createUser(request):
    """
    创建用户
    :param request: username, password, email
    :return:
    """

    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    user = MyUser.objects.filter(username=username)
    if user.exists():
        print('用户名已被注册')
        return respond_assemble(code=1, msg='用户名已被注册')
    user = MyUser.objects.filter(email=email)
    if user.exists():
        print("邮箱已被注册")
        return respond_assemble(code=1, msg='邮箱已被注册')
    else:
        user = MyUser.objects.create_user(username=username, password=password, email=email)
        print(user.get_username())
        return respond_assemble(code=0, msg='注册成功')

@require_POST
@csrf_exempt
def login(request):
    """
    用户登录
    :return:
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    #print(username)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            print("用户登录成功")
            return respond_assemble(code=1, msg="用户登录成功")
        else:
            print("用户已登录")
            return respond_assemble(code=2, msg="用户已登录")
    else:
        print("用户名或密码错误")
        return respond_assemble(code=0, msg='用户名或密码错误')