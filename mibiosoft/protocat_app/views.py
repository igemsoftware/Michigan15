from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm, ContactFrom
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    context = {
        'title': 'ProtoCat',
        'descr': 'ProtoCat - A seamless web platform to standardize wetlab protocols. Homepage.'
    }
    return render(request, 'protocat_app/root_index.html', context)

def user_registration(request):
    form = SignUpForm(request.POST)

    context = {
        'title': 'User Registration - ProtoCat',
        'descr': 'Create your free account on Protocat now!',
        'form': form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.full_name = form.cleaned_data.get('full_name')

        if not instance.full_name:
            instance.full_name = 'John Doe'

        instance.save()
        context = {
            'title': 'Thank you!',
            'descr': 'We appreciate your dedication to better protocols'
        }

    return render(request, 'protocat_app/user_registration', context)

def user_login(request):
    # if user is already authenticated it will redirect them to their homepage
    # if not, they will be prompted to login
    if not request.user.is_authenticated():
        context = {
        'title': 'User Login Page - ProtoCat'

    }
        return render(request, 'protocat_app/login', context)
    else:
        # change this to an actual redirect, this will create the right page,
        # however, it will not change the url correctly
        user_home(request)

def user_home(request):
    if request.user.is_authenticated():
        title = 'Welcome, %s' %(request.user)
        context = {
            'title': title,
        }
        return render(request, 'protocat_app/user_home', context)
    else:
        # however, it will not change the url correctly
        user_login(request)


def contact(request):
    # Add somekind of email forwarding or processing to this database
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_messages = form.cleaned_data('message')
        full_name = form.cleaned_data.get('full_name')
        subject = 'Site Contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'youotheremail@email.com']
        contact_message = '%s: %s via %s' \
                          %(full_name,
                            form_messages,
                            form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=True)
    context = {
        'form': form
    }

    return render(request, 'protocat_app/contact.html', context)


# TODO: Build views for more pages:
#     1. About
#     2. Contact
#     3. Login
#     4. User Homepage
#     5. User Settings
#     6. Protocol Entry
#     7. Protocol Presentation
#     8. How to and troubleshooting

