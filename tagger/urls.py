from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #path to return tagger.site html
    path('', views.index, name='index'),
    #path to return data based on discogsURL in request body
    path('discogsURL/', views.discogsURL, name='discogsURL'),
]
