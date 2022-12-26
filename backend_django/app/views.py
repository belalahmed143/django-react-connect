from django.shortcuts import render
from .models import *
from .serializers import ContactUsSerializer
from rest_framework.generics import ListAPIView

class ContactUsListAPIView(ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer



