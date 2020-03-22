from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
import logging
from django import forms
from .models import User
from .forms import UserForm
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    # return HttpResponse("OK")
    return render(request, 'login/index.html')

def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = User.objects.get(name=username)
            except:
                message = '用户不存在！'
                return render(request, 'login/login.html', {'message': message})

            if user.password == password:
                print(username, password)
                return redirect('user:index')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
        # return redirect('user:index')
    login_form = UserForm()
    return render(request, 'login/login.html', locals())

def login1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        message = '请检查填写的内容！'
        if username.strip() and password:
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = User.objects.get(name=username)
            except:
                message = '用户不存在！'
                return render(request, 'login/login.html', {'message': message})

            if user.password == password:
                print(username, password)
                return redirect('user:index')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
        # return redirect('user:index')
    return render(request, 'login/login.html')


def register(request):
    return render(request, 'login/register.html')

def logout(request):
    return redirect("user:login/")
