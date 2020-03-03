from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from .models import *

# Create your views here.
def index(request):
    # # 加载模板 render() 渲染模板

    # 这种方法渲染有问题，注释标记
    # tmp = loader.get_template('booktest/index.html')
    # book_list = BookInfo.manager1.all()
    # context = RequestContext(request, {'book_list': book_list})
    # return HttpResponse(tmp.reader(context))

    # return render(request, 'booktest/index.html')
    # return render(request, 'booktest/index.html', {'h1': 'hello'})
    # context = {'h1': 'hello'}
    # return render(request, 'booktest/index.html', context)
    book_list = BookInfo.manager1.all()
    context = {'book_list': book_list}
    return render(request, 'booktest/index.html', context)


def detail(request, id):
    base_manager = BookInfo.manager2.all()
    book = base_manager.get(id=id)
    context = {'book': book}
    return render(request, 'booktest/detail.html', context)

def delete(request, id):
    return HttpResponse("删除成功！")

def edit(request, id):
    return HttpResponse("编辑成功！")

def add(request):
    return HttpResponse("新增成功！")