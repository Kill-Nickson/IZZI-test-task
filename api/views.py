from datetime import datetime

from rest_framework import generics

from users.models import CustomUser
from .serializers import CustomUserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserByDateListAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        if self.request.query_params.get('date_joined') is not None:
            date_joined = datetime.strptime(self.request.query_params.get('date_joined'), '%Y-%m-%d')
            if date_joined is not None:
                queryset = queryset.filter(date_joined=date_joined)
                return queryset
        return None
