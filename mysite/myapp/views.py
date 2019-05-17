import json
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
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
    try:
        subject_friend = models.Friend.objects.get(current_user=user)
    except ObjectDoesNotExist:
        their_friend_list = []
    else:
        their_friend_list = subject_friend.users.all()
    if request.user.is_authenticated:
        try:
            you_friend = models.Friend.objects.get(current_user=request.user)
        except ObjectDoesNotExist:
            your_friend_list = []
        else:
            your_friend_list = you_friend.users.all()
    else:
        your_friend_list = []
    context = {
        "header":name + "'s Profile",
        "title":name,
        "item_list":i_list,
        "comm_form":forms.CommentForm(),
        "comments":comm_list,                    ##doesn't scale, change later
        "their_friends":their_friend_list,
        "your_friends":your_friend_list,
        "subject":user
    }
    return render(request, "profile.html", context=context)

def chirps_json(request):
    i_list = models.Chirp.objects.all()
    resp_list = {}
    resp_list["chirps"] = []
    curr_user = ""
    if request.user.is_authenticated:       ##not the most efficient way to do this
        curr_user = request.user.username   ##user is encoded with every object instead of just once
    for item in reversed(i_list):
        comments_list = []
        comm_list = models.Comment.objects.filter(comment_chirp=item)
        for comm in comm_list:
            comments_list += [{
                "comment":comm.comment_field,
                "author":comm.comment_author.username,
                "id":comm.id,
                "created_on":comm.created_on.strftime("%-m/%-d/%Y at %-I:%M:%S%p"),
                "current_user":curr_user        ##not the most efficient way to do this
            }]
        resp_list["chirps"] += [{
            "chirp":item.chirp_field,
            "author":item.chirp_author.username,
            "id":item.id,
            "comments":comments_list,
            "created_on":item.created_on.strftime("%-m/%-d/%Y at %-I:%M:%S%p"),
            "current_user":curr_user        ##not the most efficient way to do this
        }]
    return JsonResponse(resp_list)

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
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
    return redirect(request.META.get('HTTP_REFERER'))

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
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect("/")

@login_required(login_url="/login/")
def delete_chirp_view(request, chirp):
    try:
        models.Chirp.objects.get(id=chirp)
    except ObjectDoesNotExist:
        return redirect("/")
    if request.method == "POST":
        models.Chirp.objects.get(id=chirp).delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect("/")

@login_required(login_url="/login/")
def delete_comment_view(request, comment):
    try:
        models.Comment.objects.get(id=comment)
    except ObjectDoesNotExist:
        return redirect("/")
    if request.method == "POST":
        models.Comment.objects.get(id=comment).delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect("/")

@login_required(login_url="/login/")
def room_select_view(request):
    context = {
        "header":"Chat Room Select",
        "title":"Room Select"
    }
    return render(request, "chat/room_select.html", context=context)

@login_required(login_url="/login/")
def room_view(request, room_name):
    context = {
        "header":room_name,
        "title":room_name,
        'room_name_json': mark_safe(json.dumps(room_name))
    }
    return render(request, 'chat/room.html', context=context)

def change_friends(request, operation, user):
    try:
        friend = User.objects.get(id=user)
    except ObjectDoesNotExist:
        return redirect("/")
    if request.method == "POST":
        if operation == 'add':
            models.Friend.make_friend(request.user, friend)
        elif operation == 'remove':
            models.Friend.lose_friend(request.user, friend)
    return redirect(request.META.get('HTTP_REFERER'))
