from django.shortcuts import render
#from django.utils.html import escape
#from django.http import HttpResponse
# Create your views here.

from . import models
from . import forms

def index(request):
    if request.method == "POST":
        form_instance = forms.ToDoForm(request.POST)
        if form_instance.is_valid():
            #message = escape(form_instance.cleaned_data['suggestion_field'])
            #print(message)
            new_sugg = models.ToDoItem()
            new_sugg.todo_field = form_instance.cleaned_data["todo_field"]
            new_sugg.save()
            form_instance = forms.ToDoForm()
    else:
        form_instance = forms.ToDoForm()
    i_list = models.ToDoItem.objects.all()
    context = {
        "header":"CINS465 To Do List",
        "title":"CINS465 To Do List",
        "item_list":i_list,
        "form":form_instance
    }
    return render(request, "home.html", context=context)

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
