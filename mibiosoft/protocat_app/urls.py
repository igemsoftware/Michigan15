from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='root_index'),
    url(r'^contact', views.contact, name='contact'),
]
