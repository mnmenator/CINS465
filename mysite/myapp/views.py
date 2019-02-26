from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

from . import models

def index(request):
    i_list = models.Suggestion.objects.all()
    context = {
        "header":"CINS465 Home",
        "title":"CINS465 Home",
        "item_list":i_list
    }
    return render(request, "page.html", context=context)

def helloworld(request):
    context = {
        "header":"CINS465 Hello World",
        "title":"CINS465 Hello World",
    }
    return render(request, "helloworld.html", context=context)

def page_view(request, page):
    i_list = []
    p_range = page*10
    for i in range(20*(page+1)):
        i_list += ["Item "+str(i)]
    context = {
        "header":"CINS465 Pages",
        "title":"CINS465 Pages",
        "item_list":i_list[p_range:p_range+10],
        "page":page,
        "next":page+1
    }
    return render(request, "page.html", context=context)
