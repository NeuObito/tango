# -*- coding=utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="rango_index"),
	url(r'^about/$', views.about, name="rango_about"),
	url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name="rango_category"),
	url(r'^category/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'),
	url(r'^register/$', views.register, name='rango_register'),
	url(r'^login/$', views.login, name='rango_login'),
	url(r'^logout/$', views.logout, name='rango_logout'),
]
