from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('avengers', views.avengers, name='avengers'),
    path('batman', views.batman, name='batman'),
    path('search', views.search, name='search'),
    #path('add', views.add, name='add'),
    path('get', views.get, name='get'),
    path('getdata', views.getdata, name='get'),
]

