from django.urls import path
from .views import UserListAPIView, UserByDateListAPIView


urlpatterns = [
    path('users/', UserListAPIView.as_view()),
    path('users/date_joined/', UserByDateListAPIView.as_view()),
]
