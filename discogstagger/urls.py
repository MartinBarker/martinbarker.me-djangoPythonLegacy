from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #go to discogstagger.site
    path('', views.index, name='index'),
    #path('discogsURL/', views.discogsURL, name='discogsURL'),
]
