from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import UserRegistrationForm, UserAuthenticationForm, ProtocolUploadForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.core import exceptions
from django.utils import timezone
from django.contrib.auth.decorators import login_required


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

        return HttpResponse('You have successfully registered')

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


def protocol_display(request):
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
            instance.title = form.cleaned_data.get('title')
            instance.author = request.user
            instance.protocol_type = form.cleaned_data.get('protocol_type')
            instance.rating = 0.00
            instance.reagents = form.cleaned_data.get('reagents')
            instance.protocol = form.cleaned_data.get('protocol')
            instance.date_of_upload = form.cleaned_data.get('date_of_upload')
            instance.save()
            return HttpResponse('You have posted a protocol')

        else:
            return render(request, 'protocat_app/protocol_upload.html', context)
    else:
        return HttpResponseRedirect('/user_authentication/')

