from django.shortcuts import render
from django.contrib.auth import get_user_model
from copy import deepcopy

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer


user_model = get_user_model()


class UserViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = user_model.objects.all()
    # lookup_field = "id"
    permission_classes_by_action = {'create': [AllowAny], "retrieve": [IsAuthenticated],
                                    'list': [IsAdminUser], "update": [IsAuthenticated, IsAdminUser]
                                    }

    def create(self, request, *args, **kwargs):
        data = deepcopy(request.data).dict()
        email, password = data.pop("email"), data.pop("password")
        user_inst = user_model.objects.create(email, password, **data)
        ser = self.get_serializer(user_inst)
        return Response(ser.data, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

