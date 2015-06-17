from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf.urls.static import static

#default dictionary for each of the pages
page = {
    'title': 'ProtoCat',
    'descr': 'ProtoCat - A seamless web platform to standardize wetlab protocols. Homepage.'
}


def index(request):
    page = {
        'title': 'ProtoCat',
        'descr': 'ProtoCat - A seamless web platform to standardize wetlab protocols. Homepage.'
    }
    return render(request, 'protocat_app/root_index.html', page,)

def user_registration(request):
    page = {
        'title' : 'User Registration - ProtoCat',
        'descr' : 'Create your free account on Protocat now!',
        'user_data' : {

        }
    }
    return render(request, 'protocat_app/user_registration', page)

# TODO: Build views for more pages:
#     1. About
#     2. Contact
#     3. Login
#     4. User Homepage
#     5. User Settings
#     6. Protocol Entry
#     7. Protocol Presentation
#     8. How to and troubleshooting

def contact(request):
    return HttpResponse('This is the contact page')

