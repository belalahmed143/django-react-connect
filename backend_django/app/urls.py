from django.urls import path
from .views import *
urlpatterns = [
    path('', ContactUsListAPIView.as_view()),
]