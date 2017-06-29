# encoding: utf-8
from django.shortcuts import render
from users.models import MyUser, UserSetting
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from newsbackend.common import respond_assemble
# 解决编码问题
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

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
    phone = request.POST.get('phone')
    user = MyUser.objects.filter(username=username)
    if user.exists():
        print('用户名已被注册')
        return respond_assemble(code=0, msg='用户名已被注册')
    user = MyUser.objects.filter(email=email)
    if user.exists():
        print("邮箱已被注册")
        return respond_assemble(code=0, msg='邮箱已被注册')
    else:
        user = MyUser.objects.create_user(username=username, password=password, email=email, phone=phone)
        setting = UserSetting.objects.create(userid=user,finance=5,sports=5,ent=5,mil=5,edu=5,tech=5,nba=5,stock=5)
        print(setting)
        print(user.get_username())
        return respond_assemble(code=1, msg='注册成功')

@require_POST
@csrf_exempt
def Mylogin(request):
    """
    用户登录
    :return:
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    #print(username)
    '''
    if request.user.is_authenticated():
        print("用户已登录")
        return respond_assemble(code=0, msg="用户已登录")
    '''
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            print("用户登录成功")
            body = dict(username=username)
            return respond_assemble(code=1, msg="用户登录成功", body=body)
        else:
            print("用户已冻结")
            return respond_assemble(code=0, msg="用户已冻结")
    else:
        print("用户名或密码错误")
        return respond_assemble(code=0, msg='用户名或密码错误')


@csrf_exempt
def islogin(request):
    """
    验证用户是否登录
    :param request:
    :return: 用户是否登录
    """
    if request.user.is_authenticated():
        print("用户已经登录了")
        body = dict(username=request.user.get_username())
        return respond_assemble(code=1, msg="用户已经登录",body=body)
    else :
        print("用户未登录")
        return respond_assemble(code=0, msg="用户未登录")

@csrf_exempt
def Mylogout(request):
    """
    用户注销
    :param request:
    :return: 是否注销成功
    """
    logout(request)
    return respond_assemble(code=0, msg='用户登出成功')

@csrf_exempt
@require_POST
def setlike(request):
    """
    设置用户喜好
    :param request:
    :return:
    """
    finance = request.POST.get('finance')
    print(finance)
    return respond_assemble(code=0, msg='设置偏好成功')