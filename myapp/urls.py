from django.urls import path
from myapp.views import *

urlpatterns = [
    path('register/',Register.as_view()),
]
