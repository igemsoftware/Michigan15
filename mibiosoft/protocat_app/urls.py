from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='root_index'),
    url(r'^user_authentication/', views.user_authentication, name='user_login'),
    url(r'^user_registration/', views.user_registration, name='user_registration'),
    url(r'^protocol_display/(?P<protocol_id>[0-9]+)/$', views.protocol_display, name='protocol_display'),
    url(r'^user_home/', views.user_home, name='user_display'),
    url(r'^protocol_upload/', views.protocol_upload, name='protocol_upload'),
    url(r'^user_logout/', views.user_logout, name='user_logout'),
    url(r'^protocol_list/', views.protocol_list, name='protocol_list'),
    url(r'^rating_list/', views.protocol_list_rating, name='protocol_list_rating'),
    url(r'^date_list/', views.protocol_list_date, name='protocol_list_date'),
    url(r'^author_list/', views.protocol_list_author, name='protocol_list_author'),
    url(r'^title_list/', views.protocol_list_title, name='protocol_list_title'),
    url(r'^modified_list/', views.protocol_list_modified, name='protocol_list_modified'),
    url(r'^delete_protocol/(?P<protocol_id>[0-9]+)/$', views.delete_protocol, name='delete_protocol'),
    url(r'^pre_edit/(?P<protocol_id>[0-9]+)/$', views.pre_edit, name='pre_edit'),
    url(r'^edit_protocol/(?P<protocol_id>[0-9]+)/$', views.edit_protocol, name='edit_protocol'),
    url(r'^search/$', views.search, name='search'),
    url(r'^rating/(?P<protocol_id>[0-9]+)/$', views.rating, name='rating'),
    url(r'^about/', views.about, name='about'),
]
