from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'$', views.index, name='index'),
	url(r'^animals/$', views.listing, name='listing'),
	url(r'^animals/category/$', views.category, name='category'),
	url(r'^animals/(?P<id>[0-9]+)/$', views.result, name='result'),
]