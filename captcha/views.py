from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from captcha.serializers2 import CommentSerializer

# Create your views here.
class CommentView(APIView):

    def get(self, request):
        return Response({'message':'hi'})

    def post(self,request):
        serializer = CommentSerializer(data = request.data)
        print(serializer)
        # print(serializer.data)
        
        submitted = False
        if serializer.is_valid():
            submitted = True
        return Response({'submitted': submitted})