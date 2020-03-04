from django.shortcuts import render
from django.urls import reverse
from django.http import *
from django.core.paginator import Paginator
from .models import *
from django_test import settings
import base64
import cv2
import time
import os

# Create your views here.
def index(request):
    # # 加载模板 render() 渲染模板
    # return render(request, 'booktest/index.html')
    # return render(request, 'booktest/index.html', {'h1': 'hello'})
    # context = {'h1': 'hello'}
    # return render(request, 'booktest/index.html', context)
    # abc = int('abc') # 此处应用与中间件类（SystemException）测试
    book_list = BookInfo.manager1.all()
    context = {'book_list': book_list}
    return render(request, 'booktest/index.html', context)

def list(request, pIndex):
    data_list = BookInfo.manager1.filter(isDelete=False)
    p = Paginator(data_list, 10)

    if pIndex == "":
        pIndex = 1
    pIndex = int(pIndex)
    data_list2 = p.page(pIndex)
    plist = p.page_range #　所有页码
    context = {
        "list": data_list2,  # 分好页后的数据
        "plist": plist,  # 页码列表
        "pIndex": pIndex,  # 当前页码
    }
    return render(request, 'booktest/list.html', context)


def list1(request, pIndex, pSize = 10):
    data_list = BookInfo.manager1.filter(isDelete=False)
    p = Paginator(data_list, pSize)

    if pIndex == "":
        pIndex = 1
    pIndex = int(pIndex)
    data_list2 = p.page(pIndex)
    plist = p.page_range #　所有页码
    context = {
        "list": data_list2,  # 分好页后的数据
        "plist": plist,  # 页码列表
        "pIndex": pIndex,  # 当前页码
    }
    return render(request, 'booktest/list.html', context)


def detail(request, id):
    base_manager = BookInfo.manager2.all()
    book = base_manager.get(id=id)
    context = {'book': book}
    return render(request, 'booktest/detail.html', context)

def detail1(request, id):
    base_manager = BookInfo.manager2.all()
    book = base_manager.get(id=id)
    context = {'book': book}
    # 使用url的反解析，模板上配合url标签一起使用
    return reverse('detail', context)
    # return render(request, 'booktest/detail.html', context)

def delete(request, id):
    return HttpResponse("删除成功！")

def delete1(request, id):
    return HttpResponse("删除成功！")

def edit(request, id):
    return HttpResponse("编辑成功！")

def add(request):
    bname = request.POST['bname']
    base_manager = BookInfoManager()
    base_manager.create({"name"})
    return HttpResponse("新增成功！")

# 上传图片
def to_upload(request):
    return render(request, 'booktest/upload.html')


# 上传图片
def upload(request):
    if request.method == "POST":
        f1 = request.FILES['pic']
        genernal_part = "/" + time.strftime('%Y-%m-%d', time.localtime(time.time()))
        fpath = settings.MEDIA_ROOT + genernal_part

        if not os.path.exists(fpath):
            os.makedirs(fpath)

        fname = fpath + "/" + f1.name
        img_path = genernal_part + "/" + f1.name
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
            return JsonResponse({'message': 'success', 'img_path': img_path})
    else:
        # return render(request, "booktest/upload.html", {"error": "上传失败"})
        return JsonResponse({'message': 'failed'})