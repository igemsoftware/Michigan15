from django.shortcuts import render, HttpResponse, HttpResponseRedirect
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
        return HttpResponseRedirect('/user_authentication/')

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
                context.banner = ('The password is valid, but the account has been diasbled! User: ' + form.cleaned_data.get('user_name'))
        else:
            return HttpResponse('the user name and password were incorrect')

        if user.is_autheniticated():
            return HttpResponse('<h1>You are currently logged in.</h1>')

    return render(request, 'protocat_app/user_authentication.html', context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def protocol_display1(request):
    context = {
        'title': 'You are currently viewing the template display model',
        'descr': 'This is the template protocol -- DEVELOPMENT ONLY',
    }
    return render(request, 'protocat_app/protocol_display.html', context)

def user_home(request):
    context = {
        'title': 'XYZ Profile Page',
        'descr': 'this is the homepage of user XYZ'
    }

    return render(request, 'protocat_app/user_home.html', context)

@login_required(login_url='/user_authentication')
def protocol_upload(request):
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
            instance.reagents = form.cleaned_data.get('reagents')
            instance.protocol = form.cleaned_data.get('protocol')
            instance.date_of_upload = datetime.now()
            instance.save()
            return HttpResponse('You have posted a protocol')

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
    protocol_list=[]


    for each in Protocol.objects.all():
        title = each.title
        author = each.author
        date = each.date_of_upload
        protocol_id = each.id
        url = "/protocol_display/" + str(protocol_id)
        inner_protocol = [title, author, date, protocol_id, url]
        protocol_list.append(inner_protocol)

    return render(request,'protocat_app/protocol_list.html', {'protocol_list':protocol_list})

def protocol_display(request, protocol_id):
    protocol_items = Protocol.objects.get(id=protocol_id)

    return render(request, 'protocat_app/protocol_display.html', {'protocol_items':protocol_items})

def delete_protocol(request, protocol_id):
    protocol = Protocol.objects.get(id=protocol_id)
    protocol.delete()

    return HttpResponseRedirect('/protocol_list/')

def edit_protocol(request, protocol_id):
    protocol = Protocol.objects.get(id=protocol_id)
    form = ProtocolUploadForm(request.GET, instance=protocol)
    url= "/protocol_display/" + str(protocol_id) + "/"

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



