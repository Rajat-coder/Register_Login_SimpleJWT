from django.shortcuts import render
from rest_framework.views import APIView
from myapp.serializers import *
from rest_framework import status
from rest_framework.response import Response

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

