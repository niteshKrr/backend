from django.urls import path
from django.conf.urls import url 
from . import views
urlpatterns = [
    #path('', views.apiOverview, name='apiOverview'),
   url(r'^medicino/$', views.ShowAll),
   url(r'^medicino/(?P<pk>[0-9]+)$', views.ViewMedicine),
]