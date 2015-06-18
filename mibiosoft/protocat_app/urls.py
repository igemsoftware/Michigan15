from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='root_index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^user_registration/', views.user_registration, name='user_registration'),
    url(r'^login/', views.user_login, name='login_attempt'),
    url(r'^user_home/', views.user_home, name='user_home'),
]
