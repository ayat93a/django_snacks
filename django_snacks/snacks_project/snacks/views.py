from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    # model = Home

class AboutTemplateView(TemplateView):
    template_name: str = 'about.html'
    # model = About