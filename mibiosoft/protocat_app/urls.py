from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='root_index'),
    url(r'^user_authentication/', views.user_authentication, name='user_login'),
    url(r'^user_registration/', views.user_registration, name='user_registration'),
]
