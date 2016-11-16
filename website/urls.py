from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^thanks/', views.contact, name='thanks'),
	url(r'^about/', views.about, name='about')
]