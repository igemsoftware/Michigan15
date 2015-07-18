from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='root_index'),
    url(r'^user_authentication/', views.user_authentication, name='user_login'),
    url(r'^user_registration/', views.user_registration, name='user_registration'),
    url(r'^protocol_display/', views.protocol_display, name='protocol_display'),
    url(r'^user_home/', views.user_home, name='user_display'),
    url(r'^protocol_upload/', views.protocol_upload, name='protocol_upload'),
    url(r'^user_logout/', views.user_logout, name='user_logout'),
]
