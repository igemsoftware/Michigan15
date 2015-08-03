from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import HttpRequest
from .forms import UserRegistrationForm, UserAuthenticationForm, ProtocolUploadForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.core import exceptions
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required
from protocat_app.models import *


def index(request):
    context = {
        'title': 'ProtoCat',
        'descr': 'ProtoCat - A seamless web platform to standardize wetlab protocols. Homepage.'
    }
    return render(request, 'protocat_app/root_index.html', context)
# add set test cookie

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'protocat_app/about.html', context)
    
def user_registration(request):
    form = UserRegistrationForm(request.POST)

    context = {
        'title': 'User Registration - ProtoCat',
        'descr': 'Create your free account on Protocat now!',
        'form': form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user_name = form.cleaned_data.get('user_name')
        instance.email = form.cleaned_data.get('email')
        instance.password = form.cleaned_data.get('password')
        user = User.objects.create_user(instance.user_name, instance.email, instance.password)
        user = authenticate(username=instance.user_name, password=instance.password)
        if user is not None:
            # the pasword verified for the user
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/user_home/')

    return render(request, 'protocat_app/user_registration.html', context)


def user_authentication(request):
    # not working...
    if request.user.is_authenticated():
        return HttpResponse('You are already logged in')

    form = UserAuthenticationForm(request.POST)
    context = {
        'title': 'User Authentication - ProtoCat',
        'descr': 'User Authentication --> Because why not!',
        'form': form
    }

    if form.is_valid():
        user = authenticate(username = form.cleaned_data.get('user_name'), password=form.cleaned_data.get('password'))


        if user is not None:
            # the pasword verified for the user
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/user_home/')

            else:
                context.banner = ('The password is valid, but the account has been disabled! User: ' + form.cleaned_data.get('user_name'))
        else:
            return HttpResponse('the user name and password were incorrect')

        if user.is_authenticated():
            return HttpResponse('<h1>You are currently logged in.</h1>')

    return render(request, 'protocat_app/user_authentication.html', context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_home(request):
    context = {
        'title': 'XYZ Profile Page',
        'descr': 'this is the homepage of user XYZ'
    }

    return render(request, 'protocat_app/user_home.html', context)

@login_required(login_url='/user_authentication')
def protocol_upload(request):

    x = 0
    text = ''
    newline = '\n'
    while request.POST.get('step' + str(x)):
        text += (request.POST.get('step' + str(x)))
        text += newline
        x += 1

    if User.is_authenticated:
        form = ProtocolUploadForm(request.POST)
        context = {
                'title': 'Protocol Upload',
                'form': form
            }
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id=form.cleaned_data.get('id')
            instance.title = form.cleaned_data.get('title')
            instance.author = request.user
            instance.protocol_type = form.cleaned_data.get('protocol_type')
            instance.rating = 0.00
            instance.num_ratings = 0
            instance.user_rated = [0]
            instance.reagents = form.cleaned_data.get('reagents')
            instance.protocol_steps = text
            instance.date_of_upload = datetime.now()
            instance.save()
            return HttpResponseRedirect('/protocol_list')

        else:
            return render(request, 'protocat_app/protocol_upload.html', context)
    else:
        return HttpResponseRedirect('/user_authentication/')

def protocol_list(request):

    all_entries = Protocol.objects.all()
    title = ''
    author = ''
    date = ''
    id=''
    rating=''
    protocol_list=[]


    for each in Protocol.objects.all():
        title = each.title
        author = each.author
        date = each.date_of_upload
        protocol_id = each.id
        rating = each.rating
        url = "/protocol_display/" + str(protocol_id)
        inner_protocol = [title, author, date, protocol_id, url, rating]
        protocol_list.append(inner_protocol)

    return render(request,'protocat_app/protocol_list.html', {'protocol_list':protocol_list})

def protocol_display(request, protocol_id):
    protocol_items = Protocol.objects.get(id=protocol_id)
    steps = protocol_items.protocol_steps
    current_user = str(request.user)

    return render(request, 'protocat_app/protocol_display.html', {'protocol_items':protocol_items, 'steps':steps,
                                                                  'current_user':current_user})

def delete_protocol(request, protocol_id):
    protocol = Protocol.objects.get(id=protocol_id)
    protocol.delete()

    return HttpResponseRedirect('/protocol_list/')

def edit_protocol(request, protocol_id):
    protocol = Protocol.objects.get(id=protocol_id)
    form = ProtocolUploadForm(request.GET, instance=protocol)
    url= "/protocol_display/" + str(protocol_id)

    if request.POST:
        form = ProtocolUploadForm(request.POST)

    if form.is_valid():

        protocol = Protocol.objects.get(id=protocol_id)
        form = ProtocolUploadForm(request.POST, instance = protocol)
        form.save()
        return HttpResponseRedirect(url)
    else:
        context = {
            'title': 'Protocol Edit',
            'form': form
        }
        protocol = Protocol.objects.get(pk = protocol_id)
        form = ProtocolUploadForm(instance=protocol)

        return render(request,'protocat_app/edit_protocol.html',context)

def search(request):
    query = request.GET.get('search')
    if query:
        results = Protocol.objects.filter(title__contains=query)
    else:
        results = ''
    return render(request, 'protocat_app/search_protocols.html',{'results':results})

def rating(request, protocol_id):
    rate = str(request.POST.get('rating'))
    protocol = Protocol.objects.get(id=protocol_id)
    protocol.rating = protocol.rating * protocol.num_ratings
    protocol.num_ratings += 1
    protocol.rating += int(rate)
    protocol.rating = protocol.rating / protocol.num_ratings
    current_user = str(request.user)
    protocol.user_rated += current_user
    protocol.save()
    url = "/protocol_display/" + str(protocol_id) + "/"

    return HttpResponseRedirect(url)
