from django.shortcuts import render
from django.http import HttpResponse
from psql.models import *


# Create your views here.
def index(request):
    bings = Bing.objects.all()
    return render(request, 'index.html', {'bings': bings})
