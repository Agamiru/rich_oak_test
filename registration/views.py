from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


user_model = get_user_model()


class UserViewSet(viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = user_model.objects.all()
    # lookup_field = "id"

