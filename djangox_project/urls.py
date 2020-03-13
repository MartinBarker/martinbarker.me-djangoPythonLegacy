from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.apps import apps
from allauth.account.views import confirm_email as allauthemailconfirmation
import re
from django.conf.urls import url
from rest_framework_jwt.views import refresh_jwt_token
from django.contrib.auth import views as auth_views

from django.urls import reverse

urlpatterns = [
    #all tagger paths go to tagger/urls.py
    path('tagger/', include('tagger.urls')),
    #all discogstagger paths go to discogstagger/urls.py
    path('discogstagger/', include('discogstagger.urls')),

    #tagger.site
    #path('tagger', include('martinbarker.urls')),
    #path('taggerpy', include('martinbarker.urls')),

    #admin page
    path('admin/', admin.site.urls),
    #path('admin/', include('django.contrib.admin.urls')),
    #playlist page
    path('playlist/', include(('playlist.urls', 'playlist'), namespace='playlist')),
    #users
    path('users/', include('django.contrib.auth.urls')),
    #accounts (allauth)
    path('accounts/', include('allauth.urls')),
    
    #songsweeper URLS
    path('songsweeper/', include('pages.urls')),
    
    #default goes to martinbarker home page
    path('', include('martinbarker.urls')),
    #path('/', include('martinbarker.urls')),

     #all projects
    path('projects', include('martinbarker.urls')),

    
    #discogstagger.site
    #path('discogstagger', include('martinbarker.urls')),
    #discogstaggerphp file
    #path('discogstaggerphp', include('martinbarker.urls')),
    #discogstagger script python\
    #path('my-ajax-test', include('martinbarker.urls')),
    
    #popularify
    #path('popularify/', include('popularify.urls')),
    path('popularify', include('martinbarker.urls')),
    path('popularify_py', include('martinbarker.urls')),
    path('SpotifyAuth', include('martinbarker.urls')),
    path('popularify_updatePage', include('martinbarker.urls')),
    

   

    #django-rest-auth
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    #bug reports for this issue online point to a solution like so, but this isn't fixing the error
    #url(r"^rest-auth/registration/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)/$", allauthemailconfirmation, name="account_confirm_email"),
    
    url(r"^rest-auth/registration/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)", include('users.urls'), name="account_confirm_email"),

    #jwt
    url(r'^refresh-token/', refresh_jwt_token),
]


