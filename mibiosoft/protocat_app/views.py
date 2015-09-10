from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
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
import operator
from functools import reduce
from .protocols import PROTOCOL_TYPES
from django.db.models.functions import Lower
from django.db.models import Func, F

'''
Add your views functions here
'''

'''
Renders the "Index" page
'''
def index(request):
    context = {
        'title': 'ProtoCat',
        'descr': 'ProtoCat - A seamless web platform to standardize wetlab protocols. Homepage.'
    }
    return render(request, 'protocat_app/root_index.html', context)

'''
Renders the "About" page
'''
def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'protocat_app/about.html', context)

'''
Uses the UserRegistrationForm in forms.py
Validates input data.
If valid, a User will be created, added to database, logged in, and redirect to user home
Else, will be sent back to registration page
'''
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
        # This if statement makes sure no usernames are the same
        if User.objects.filter(username=instance.user_name):
            context['error_message'] = "This username has been taken!"
            return render(request, 'protocat_app/user_registration.html', context)
        instance.first_name = form.cleaned_data.get('first_name')
        instance.last_name = form.cleaned_data.get('last_name')
        instance.email = form.cleaned_data.get('email')
        instance.password = form.cleaned_data.get('password')
        user = User.objects.create_user(instance.user_name, instance.email, instance.password)
        user.first_name = instance.first_name
        user.last_name = instance.last_name
        user.save()
        user = authenticate(username=instance.user_name, password=instance.password)
        if user is not None:
            # the pasword verified for the user
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/user_home/')

    return render(request, 'protocat_app/user_registration.html', context)


'''
Uses the UserAuthenticationForm in forms.py
Validates input data.
If valid, a User will be created, added to database, logged in, and redirect to user home
Else, will be sent back to login page
'''
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
            context['error'] = "The username or password you entered was incorrect."
            return render(request, 'protocat_app/user_authentication.html', context)

        if user.is_authenticated():
            return HttpResponse('<h1>You are currently logged in.</h1>')

    return render(request, 'protocat_app/user_authentication.html', context)

'''
Logs user out
'''
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

'''
Requires User to be logged in
Takes all steps and combines into one text
If form data is valid, will have to database
Else, will be sent back to Upload page
'''
@login_required(login_url='/user_authentication')
def protocol_upload(request):

    # This reads in the "protocol steps" and puts them all in to the variable "text"
    x = 1
    newline = '\n'
    text = ''

    while request.POST.get('step' + str(x)):
        text += ('Step ' + str(x))
        text += newline
        text += (request.POST.get('step' + str(x)))
        text += newline
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


'''
Displays a list of all protocols in database
'''
def protocol_list(request):

    all_entries = Protocol.objects.all().order_by('-date_modified')
    protocol_list=[]


    for each in all_entries:
        title = each.title
        author = each.author
        date = each.date_of_upload
        last_mod = each.date_modified
        protocol_id = each.id
        rating = each.rating
        url = "/protocol_display/" + str(protocol_id)
        url2 = "/user_profile/" + str(author)
        inner_protocol = [title, author, date, protocol_id, url, rating, last_mod, url2]
        protocol_list.append(inner_protocol)

    asc = 'asc'

    return render(request,'protocat_app/protocol_list.html', {'protocol_list':protocol_list, 'order':asc})


'''
Displays the current user's home with all protocols uploaded by that user
'''
def user_home(request):
    current_user = request.user
    name = get_object_or_404(User,username=current_user)
    first = name.first_name
    last = name.last_name

    user_protocols = Protocol.objects.filter(author=current_user)

    protocol_list = []

    for each in user_protocols:
        title = each.title
        author = each.author
        date = each.date_of_upload
        last_mod = each.date_modified
        protocol_id = each.id
        rating = each.rating
        url = "/protocol_display/" + str(protocol_id)
        inner_protocol = [title, author, date, protocol_id, url, rating, last_mod]
        protocol_list.append(inner_protocol)
    return render(request, 'protocat_app/user_home.html', {'protocol_list':protocol_list, 'first':first, 'last':last})

'''
Displays a user's profile, other than the current user
'''
def user_profile(request, user1):
    use_name = str(user1)
    name = User.objects.get(username=use_name)
    first = name.first_name
    last = name.last_name

    user_protocols = Protocol.objects.filter(author=use_name)

    protocol_list = []

    for each in user_protocols:
        title = each.title
        author = each.author
        date = each.date_of_upload
        last_mod = each.date_modified
        protocol_id = each.id
        rating = each.rating
        url = "/protocol_display/" + str(protocol_id)
        inner_protocol = [title, author, date, protocol_id, url, rating, last_mod]
        protocol_list.append(inner_protocol)
    return render(request, 'protocat_app/user_profile.html', {'protocol_list':protocol_list,
                                                              'first':first, 'last':last, 'user1':use_name})

'''
Displays a list of protocol depending on which attribute is chosen in ascending
or descending order
'''
def protocol_list_sort(request, type, order):

    if(order=='asc'):
        new_order='desc'
        if(type=='title'):
            all_entries = Protocol.objects.all().annotate(title_lower=Func(F(type), function='LOWER')).order_by('-title_lower')
        if(type=='author'):
            all_entries = Protocol.objects.all().annotate(author_lower=Func(F(type), function='LOWER')).order_by('-author_lower')
        if(type=='date_of_upload'):
            all_entries = Protocol.objects.all().annotate(date_lower=Func(F(type), function='LOWER')).order_by('-date_lower')
        if(type=='date_modified'):
            all_entries = Protocol.objects.all().annotate(mod_lower=Func(F(type), function='LOWER')).order_by('-mod_lower')
        if(type=='rating'):
            all_entries = Protocol.objects.all().order_by('-rating')

    if(order=='desc'):
        new_order='asc'
        if(type=='title'):
            all_entries = Protocol.objects.all().order_by(Lower('title'))
        if(type=='author'):
            all_entries = Protocol.objects.all().order_by(Lower('author'))
        if(type=='date_of_upload'):
            all_entries = Protocol.objects.all().order_by(Lower('date_of_upload'))
        if(type=='date_modified'):
            all_entries = Protocol.objects.all().order_by(Lower('date_modified'))
        if(type=='rating'):
            all_entries = Protocol.objects.all().order_by('rating')

    protocol_list=[]


    for each in all_entries:
        title = each.title
        author = each.author
        date = each.date_of_upload
        last_mod = each.date_modified
        protocol_id = each.id
        rating = each.rating
        url = "/protocol_display/" + str(protocol_id)
        url2 = "/user_profile/" + str(author)
        inner_protocol = [title, author, date, protocol_id, url, rating, last_mod, url2]
        protocol_list.append(inner_protocol)

    return render(request,'protocat_app/protocol_list.html', {'protocol_list':protocol_list, 'order': new_order})

'''
Displays a list of protocols containing the searched terms
'''
def protocol_search_sort(request, type, order, terms):

    terms_list = terms.split('+')
    q_list = []

    for term in terms_list:
        if term:
            q_list.append(Q(title__contains=term) | Q(author__contains=term) | Q(description__contains=term) | Q(reagents__contains=term) | Q(protocol_steps__contains=term))

    if(order=='asc'):
        new_order='desc'
        if(type=='title'):
            results = Protocol.objects.filter(reduce(operator.and_, q_list)).annotate(title_lower=Func(F(type), function='LOWER')).order_by('-title_lower')
        if(type=='author'):
            results = Protocol.objects.filter(reduce(operator.and_, q_list)).annotate(author_lower=Func(F(type), function='LOWER')).order_by('-author_lower')
        if(type=='date_of_upload'):
            results = Protocol.objects.filter(reduce(operator.and_, q_list)).annotate(date_lower=Func(F(type), function='LOWER')).order_by('-date_lower')
        if(type=='date_modified'):
            results = Protocol.objects.filter(reduce(operator.and_, q_list)).annotate(mod_lower=Func(F(type), function='LOWER')).order_by('-mod_lower')
        if(type=='rating'):
            results = Protocol.objects.filter(reduce(operator.and_, q_list)).order_by('-rating')

    if(order=='desc'):
        new_order='asc'
        if(type=='title'):
            results = Protocol.objects.filter(reduce(operator.and_, q_list)).order_by(Lower('title'))
        if(type=='author'):
            results = Protocol.objects.filter(reduce(operator.and_, q_list)).order_by(Lower('author'))
        if(type=='date_of_upload'):
            results = Protocol.objects.filter(reduce(operator.and_, q_list)).order_by(Lower('date_of_upload'))
        if(type=='date_modified'):
            results = Protocol.objects.filter(reduce(operator.and_, q_list)).order_by(Lower('date_modified'))
        if(type=='rating'):
            results = Protocol.objects.filter(reduce(operator.and_, q_list)).order_by('rating')

    protocol_list=[]


    for each in results:
        title = each.title
        author = each.author
        date = each.date_of_upload
        last_mod = each.date_modified
        protocol_id = each.id
        rating = each.rating
        url = "/protocol_display/" + str(protocol_id)
        url2 = "/user_profile/" + str(author)
        inner_protocol = [title, author, date, protocol_id, url, rating, last_mod, url2]
        protocol_list.append(inner_protocol)

    return render(request,'protocat_app/search_protocols.html', {'protocol_list':protocol_list, 'results':results, 'terms':terms, 'order':new_order})


'''
Displays all attributes of one protocol
'''
def protocol_display(request, protocol_id):
    protocol_items = Protocol.objects.get(id=protocol_id)
    steps = protocol_items.protocol_steps
    current_user = str(request.user)

    return render(request, 'protocat_app/protocol_display.html', {'protocol_items':protocol_items, 'steps':steps,'current_user':current_user})

'''
Deletes a protocol using protocol id
'''
def delete_protocol(request, protocol_id):
    protocol = Protocol.objects.get(id=protocol_id)
    author = protocol.author
    current_user = str(request.user)
    if current_user == author:
        protocol.delete()
    else:
        return HttpResponse('You cannot delete this protocol')
    return HttpResponseRedirect('/protocol_list/')

'''
Prepares user edits to a protocol and sends to edit protocol
'''
def pre_edit(request, protocol_id):

    protocol = Protocol.objects.get(id=protocol_id)
    author = protocol.author
    current_user = str(request.user)
    if current_user == author:

        title = protocol.title
        reagents = protocol.reagents
        protocol_type = protocol.protocol_type
        description = protocol.description
        protocol_steps = protocol.protocol_steps
        url= "/protocol_display/" + str(protocol_id)
        form = ProtocolUploadForm(request.POST, instance=protocol)
        context = {
            'protocol_id':protocol_id,
            'protocol':protocol,
            'title':title,
            'reagents':reagents,
            'description':description,
            'protocol_type':protocol_type,
            'protocol_steps':protocol_steps,
            'PROTOCOL_TYPES':PROTOCOL_TYPES,
            'url':url,
            'form':form
        }
        return render(request, 'protocat_app/edit_protocol.html', context)
    else:
        return HttpResponse('You cannot edit this protocol')

'''
Edits a protocol object in the database
'''
def edit_protocol(request, protocol_id):

    protocol = Protocol.objects.get(id=protocol_id)
    author = protocol.author
    current_user = str(request.user)

    if current_user == author:
        form = ProtocolUploadForm(request.POST, instance=protocol)
        url= "/protocol_display/" + str(protocol_id)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(url)
        else:
            context = {
                'title': 'Protocol Edit',
                'protocol_id': protocol_id,
                'form': form
            }

            return render(request,'protocat_app/edit_protocol.html',context)
    else:
        return HttpResponse('You cannot edit this protocol')

'''
Makes queries to the database for searched terms
'''
def search(request):
    terms = request.GET.get('search', '').split(' ')

    all_terms = []
    for each in terms:
        all_terms.append(each)

    joined = '+'.join(all_terms)

    q_list = []
    for term in terms:
        if term:
            q_list.append(Q(title__contains=term) | Q(author__contains=term) | Q(description__contains=term) | Q(reagents__contains=term) | Q(protocol_steps__contains=term))

    if q_list:
        results = Protocol.objects.filter(reduce(operator.and_, q_list))
    else:
        results = ''

    asc = 'asc'

    return render(request, 'protocat_app/search_protocols.html',{'results':results, 'terms':joined, 'order': asc})

'''
Adds user rating to average rating for a protocol
'''
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

'''
Displays the feedback page
'''
def feedback(request):

    return render(request, 'protocat_app/feedback.html')


