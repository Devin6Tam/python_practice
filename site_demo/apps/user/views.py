from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    # return HttpResponse("OK")
    return render(request, 'login/index.html')

def login(request):
    return render(request, 'login/login.html')


def register(request):
    return render(request, 'login/register.html')

def logout(request):
    return redirect("user:login/")
