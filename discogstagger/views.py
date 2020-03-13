from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.staticfiles.views import serve
from django.http import JsonResponse
import json
import discogs_client
import re
from pprint import pprint
import spotipy
import spotipy.util as util
import random
from datetime import datetime
import datetime

from django.http import JsonResponse

from urllib.parse import unquote

def index(request):
    context = { 'pageName': "discogstagger.site" , 'icon':'/static/images/discogstagger.png'}
    return render(request, 'discogstagger/index.html', context)
