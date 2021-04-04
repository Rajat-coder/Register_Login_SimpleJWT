from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def get_token(user_object):
    refresh = RefreshToken.for_user(user_object)
    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return token


#For getting Access Token of User in python manage.py shell
# from myapp.models import User
# from myapp.utils import get_token
# get_token(User.objects.get(id=1))["access"]