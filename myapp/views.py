from django.shortcuts import render
from rest_framework.views import APIView
from myapp.serializers import *
from rest_framework import status
from rest_framework.response import Response
from myapp.models import *

# Create your views here.


class Register(APIView):
    def post(self,request):
        output_status=False
        output_detail="Failed"
        res_status=status.HTTP_400_BAD_REQUEST
        data=[]
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            output_status=True
            output_detail="Success"
            res_status=status.HTTP_200_OK
            data=serializer.data
        else:
            data=serializer.errors
        context={
            "status":output_status,
            "detail":output_detail,
            "data":data
        }
        return Response(context,status=res_status)

class LoginView(APIView):
    def post(self,request):
        output_status=False
        output_detail="Failed"
        res_status=status.HTTP_400_BAD_REQUEST
        data=[]
        email=request.data.get("email")
        password=request.data.get("password")
        if email:
            model=User.objects.filter(email=email).first()
            if model:
                check_password=model.check_password(password)
                if check_password:
                    output_status=True
                    output_detail="Success"
                    res_status=status.HTTP_200_OK
                    data.append(get_tokens_for_user(model))
                else:
                    output_detail="Wrong password"
            else:
                output_detail="Wrong email"
        else:
            output_detail="Please provide email"
        context={
            "status":output_status,
            "detail":output_detail,
            "data":data
        }
        return Response(context,status=res_status)


