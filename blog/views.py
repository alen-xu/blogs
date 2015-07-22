from django.shortcuts import render
from django.conf import settings
# Create your views here.

def global_setting(request):
    site_name = settings.SITE_NAME
    site_url = settings.SITE_URL
    return locals()

def index(request):
    name = "wangfang"
    return render(request, 'index.html', locals())