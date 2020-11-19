from django.urls import path

from .views import login
from .views import UserCreate
from .views import MessageAPIView


urlpatterns = [
    path('login/', login),
    path('register/', UserCreate.as_view()),
    path('message/', MessageAPIView.as_view()),
]

