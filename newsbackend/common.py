# coding=utf-8
import json
from django.http import HttpResponse
from django.conf import settings

class ErrCode:
    """
    通用的错误消息
    """
    UNDEFINED_ERROR = -1  # 类型未定义的操作失败
    LOGIN_REQUIRED = 1001  # 需要登录以后才能进行操作, 或登录已超时
    PERMISSION_DENIED = 1002  # 没有执行该操作所需的权限
    OPERATING_ON_FROZEN_TARGET = 1003  # 正在操作一个被冻结的对象(如用户)
    MODIFYING_TO_FROZEN_TARGET = 1004  # 正在修改为一个已被冻结的对象(比如改成一个被冻结的地址)
    OPERATION_TOO_FREQUENTLY = 1005  # 操作过于频繁, 请稍后再试
    SERVICE_BUSY_PLEASE_WAIT = 1006  # 服务器繁忙, 请稍后再试
    PARAMETER_LOST = 1007  # 缺少必须的参数
    PARAMETER_VALUE_ILLEGAL = 1008  # 某些参数的值不满足要求
    CAN_NOT_UNDERSTAND_REQUEST = 1009  # 发送了服务器无法理解请求
    RESOURCE_OCCUPIED_BY_OTHER = 1010  # 待操作的资源已被占用, 请稍后再试
    LOGIN_DENIED = 1011  # 已登录用户不允许执行该操作
    IMG_CAPTCHA_VERIFICATION_REQUIRED = 1012  # 需要先完成图片验证码验证
    UNACCEPTABLE_PARAMS = 1013  # 传入了不允许的参数

    status_map = {
        UNDEFINED_ERROR: '类型未定义的操作失败',
        LOGIN_REQUIRED: '需要登录以后才能进行操作,或登录已超时',
        PERMISSION_DENIED: '没有执行该操作所需的权限',
        OPERATING_ON_FROZEN_TARGET: '正在操作一个被冻结的对象(如用户)',
        MODIFYING_TO_FROZEN_TARGET: '正在修改为一个已被冻结的对象(比如改成一个被冻结的地址)',
        OPERATION_TOO_FREQUENTLY: '操作过于频繁,请稍后再试',
        SERVICE_BUSY_PLEASE_WAIT: '服务器繁忙,请稍后再试',
        PARAMETER_LOST: '缺少必须的参数',
        PARAMETER_VALUE_ILLEGAL: '某些参数的值不满足要求',
        CAN_NOT_UNDERSTAND_REQUEST: '发送了服务器无法理解请求',
        RESOURCE_OCCUPIED_BY_OTHER: '待操作的资源已被占用,请稍后再试',
        LOGIN_DENIED: '已登录用户不允许执行该操作',
        IMG_CAPTCHA_VERIFICATION_REQUIRED: '需要先完成图片验证码验证',
        UNACCEPTABLE_PARAMS: '传入了不允许的参数',
    }

_INDENT = 4 if settings.DEBUG else None
_ENSURE_ASCII = not settings.DEBUG

def respond_assemble(code=0, msg='ok', body=None, extramsg=None, dbgmsg=None):
    """
    组装API响应
    :param extramsg: 额外的消息, 会以字符串连接的形式加到正常的msg之后
    :param dbgmsg: debug信息, 只有当 DEBUG 选项打开时才会加入到响应, 否则会被丢弃
    :type dbgmsg: Any
    :type extramsg: Any
    :type body: Union[None, Dict[str, str], Dict[str, bool], Dict[str, int], Dict[str, float]]
    :type msg: str
    :type code: int
    """
    resp = {
        "code": code,
        "msg": msg if code < 1000 or msg != 'ok' else ErrCode.status_map.get(code, '未知错误'),
        "body": body or [],
    }
    if extramsg is not None:
        resp['msg'] += ' ' + str(extramsg)
    if dbgmsg is not None and settings.DEBUG:
        resp['dbgmsg'] = str(dbgmsg)

    j_dmp = json.dumps(
        resp,
        ensure_ascii=_ENSURE_ASCII,
        indent=_INDENT
    )

    resp = HttpResponse(
        j_dmp,
        content_type='application/json; encoding=utf-8',
    )

    # 禁止浏览器缓存
    resp['Cache-Control'] = 'no-cache, no-store, max-age=0, must-revalidate'
    resp['Expires'] = 'Mon, 26 Jul 1997 05:00:00 GMT'

    if settings.DEBUG:
        resp['Access-Control-Allow-Credentials'] = 'true'
        print("response: ", j_dmp)
    return resp
