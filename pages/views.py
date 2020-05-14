from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(req, *arg, **kwargs):
    # return HttpResponse('./template/home/index.html')
    rend = render(req, "layout.html", {})
    return rend