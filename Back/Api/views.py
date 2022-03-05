import datetime
import os
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import *
import json
import hashlib
# Create your views here.


def index(request):
    return redirect('admin/')


def lo(request):
    res, data, meta = {}, {}, {}
    if (request.method == "POST"):
        msg = "请求成功"
        code = 200
    else:
        msg = "请求错误"
        code = 400
    res['data'] = data
    meta['msg'] = msg
    meta['code'] = code
    res['meta'] = meta
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})


def login(request):
    res, data, meta = {}, {}, {}
    if (request.method == "POST"):
        getres = json.loads(request.body)
        login_in = User.objects.filter(
            username=getres['username'], password=getres['password']).exists()
        if login_in:
            UserData = User.objects.filter(
                username=getres['username'], password=getres['password']).values('id','username', 'rid','LoginTime').first()
            token=hashlib.sha1(os.urandom(40)).hexdigest()
            data['token'] = token
            data['username'] = getres['username']
            data['rid'] = UserData['rid']
            data['LoginTime']=UserData['LoginTime']
            data['id']=UserData['id']
            User.objects.filter(username=getres['username'],password=getres['password']).update(token=token,LoginTime=datetime.datetime.now())
            msg = "请求成功"
            code = 200
        else:
            msg = "账号密码错误"
            code = 200
    else:
        msg = "请求错误"
        code = 400
    res['data'] = data
    meta['msg'] = msg
    meta['code'] = code 
    res['meta'] = meta
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})
