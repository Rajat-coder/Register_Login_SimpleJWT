from django.urls import path
from myapp.views import *
from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('register/',Register.as_view()),
    path('login/',LoginView.as_view()),
    path('get/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/token/',TokenRefreshView.as_view()),
    path('verify/token',TokenVerifyView.as_view()),
]
