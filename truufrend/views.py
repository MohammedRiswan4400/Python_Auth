from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from twilio.rest import Client
from truufrend.models import Profile,SOS,Video
from rest_framework import viewsets
from rest_framework import status
from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from truufrend.serializers import ProfileSerializer,VideoSerializer
from django.conf import settings
import vonage
from nexmo import Sms
import requests
class InitiateVerificationView(APIView):
    def post(self, request):
        print(request.data)
        ACCOUNT_SID = config('TWILIO_ACCOUNT_SID', default='')
        AUTH_TOKEN = config('TWILIO_AUTH_TOKEN', default='')
        VERIFY_SERVICE_SID = config('TWILIO_VERIFY_SERVICE_SID', default='')
        phone = "+91" + request.data.get('phone')
        if not phone:
            return Response({'error': 'phone number is requied'})
        try:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            verification = client.verify \
                .services(VERIFY_SERVICE_SID) \
                .verifications \
                .create(to=phone, channel='sms')
            return Response({'message': 'Verification initiated.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyUserView(APIView):
    def post(self, request):
        ACCOUNT_SID = config('TWILIO_ACCOUNT_SID', default='')
        AUTH_TOKEN = config('TWILIO_AUTH_TOKEN', default='')
        VERIFY_SERVICE_SID = config('TWILIO_VERIFY_SERVICE_SID', default='')
        print(request.data)
        phone = "+91" + request.data.get('phone')
        code = request.data.get('code')
        print(phone)
        if not phone or not code:
            return Response({'error': 'Phone number and code are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            verification_check = client.verify \
                .services(VERIFY_SERVICE_SID) \
                .verification_checks \
                .create(to=phone, code=code)
            if verification_check.status == 'approved':
                # Create or update user object here
                return Response({'message': 'User verified.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class Nickname(APIView):
    def post(self,request):
        nick_name=request.data.get('nick_name')
        n = Profile.objects.create(nick_name=nick_name)
        n.save()
        return Response({'message': 'nick_name added'}, status=status.HTTP_200_OK)
class Age(APIView):
    def post(self,request):
        age=request.data.get('age')
        a=Profile.objects.create(age=age)
        a.save()
        return Response({'message': 'age added'}, status=status.HTTP_200_OK)
class AddChallenges(APIView):
    def post(self,request):
        challenges=request.data.get('challenges')
        a = Profile.objects.create(challenges=challenges)
        a.save()
        return Response({'message': 'Challenges added'}, status=status.HTTP_200_OK)
class CreateSOS(APIView):
    def post(self,request):
        contact=request.data.get('contact')
        c=SOS.objects.create(contact=contact)
        c.save()
        return Response({'message': 'SOS contact added'}, status=status.HTTP_200_OK)
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer








