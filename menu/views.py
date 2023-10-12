from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class TestView(TemplateView):
    template_name = 'base.html'

class HelloWorldView(TemplateView):
    template_name = 'hello_world.html'
