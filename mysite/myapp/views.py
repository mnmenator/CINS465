from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
#from django.utils.html import escape
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
# Create your views here.

from . import models
from . import forms

#@login_required(redirect_field_name='/', login_url="/login/")
def index(request):
    if request.method == "POST":
        form_instance = forms.ChirpForm(request.POST)
        if form_instance.is_valid():
            new_chirp = models.Chirp()
            new_chirp.chirp_field = form_instance.cleaned_data["chirp_field"]
            new_chirp.chirp_author = request.user
            new_chirp.save()
            form_instance = forms.ChirpForm()
    else:
        form_instance = forms.ChirpForm()
    i_list = models.Chirp.objects.all()
    context = {
        "header":"Home",
        "title":"Chatter",
        "item_list":i_list,
        "form":form_instance,
        "comm_form":forms.CommentForm()
    }
    return render(request, "home.html", context=context)

def profile_view(request, name):
    try:
        user = User.objects.get(username=name)
    except ObjectDoesNotExist:
        return redirect("/")
    i_list = models.Chirp.objects.filter(chirp_author=user)
    i_list = reversed(i_list)
    comm_list = models.Comment.objects.all()    ##doesn't scale, change later
    context = {
        "header":name + "'s Profile",
        "title":name,
        "item_list":i_list,
        "comm_form":forms.CommentForm(),
        "comments":comm_list                    ##doesn't scale, change later
    }
    return render(request, "profile.html", context=context)

def chirps_json(request):
    i_list = models.Chirp.objects.all()
    resp_list = {}
    resp_list["chirps"] = []
    for item in reversed(i_list):
        comments_list = []
        comm_list = models.Comment.objects.filter(comment_chirp=item)
        for comm in comm_list:
            comments_list += [{
                "comment":comm.comment_field,
                "author":comm.comment_author.username,
                "id":comm.id,
                "created_on":comm.created_on
            }]
        resp_list["chirps"] += [{
            "chirp":item.chirp_field,
            "author":item.chirp_author.username,
            "id":item.id,
            "comments":comments_list,
            "created_on":item.created_on
        }]
    return JsonResponse(resp_list)

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            ##user = form_instance.save()
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/login/")
def comment_view(request, chirp):
    try:
        models.Chirp.objects.get(id=chirp)
    except ObjectDoesNotExist:
        return redirect("/")
    if request.method == "POST":
        form_instance = forms.CommentForm(request.POST)
        if form_instance.is_valid():
            chirp_instance = models.Chirp.objects.get(id=chirp)
            new_comment = models.Comment()
            new_comment.comment_field = form_instance.cleaned_data["comment_field"]
            new_comment.comment_chirp = chirp_instance
            new_comment.comment_author = request.user
            new_comment.save()
            return redirect("/")
    else:
        form_instance = forms.CommentForm()
    context = {
        "body":"",
        "title":"",
        "form":form_instance,
        "chirp":chirp
    }
    return render(request, "comment.html", context=context)
