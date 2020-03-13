from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.apps import apps
from allauth.account.views import confirm_email as allauthemailconfirmation
from django.conf.urls import url
from rest_framework_jwt.views import refresh_jwt_token
from django.contrib.auth import views as auth_views
from django.urls import reverse
import re

urlpatterns = [
    #default goes to martinbarker home page
    path('', include('martinbarker.urls')),
    #all projects
    path('projects', include('martinbarker.urls')),

    #all tagger paths go to tagger/urls.py
    path('tagger/', include('tagger.urls')),
    #discogstagger: redirect to discogstagger/urls.py
    path('discogstagger/', include('discogstagger.urls')),

    #admin page
    path('admin/', admin.site.urls),
    path('playlist/', include(('playlist.urls', 'playlist'), namespace='playlist')),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('songsweeper/', include('pages.urls')),

    #popularify
    path('popularify', include('martinbarker.urls')),
    path('popularify_py', include('martinbarker.urls')),
    path('SpotifyAuth', include('martinbarker.urls')),
    path('popularify_updatePage', include('martinbarker.urls')),
    
    #django-rest-auth
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r"^rest-auth/registration/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)", include('users.urls'), name="account_confirm_email"),
    url(r'^refresh-token/', refresh_jwt_token),
]


