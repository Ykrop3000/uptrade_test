from django.urls import path

from menu.views import TestView, HelloWorldView

urlpatterns = [
    path('', TestView.as_view(), name='home'),
    path('hello_world/', HelloWorldView.as_view(), name='hello_world'),

]
