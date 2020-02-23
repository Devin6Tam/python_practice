from django.shortcuts import render
from django.http import *

# Create your views here.
def index(request):
    # # 加载模板 render() 渲染模板
    # tmp = loader.get_template('booktest/index.html')
    # return HttpResponse(tmp.render())
    return render(request, 'booktest/index.html')