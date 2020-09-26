from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .utils import ObjectDetailMixin

# Create your views here.

# def index(request):
#     return render(request, 'base.html')

class Index(ObjectDetailMixin, View):
    template = 'base.html'

