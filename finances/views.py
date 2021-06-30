from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from .serializers import AccountDetailsSerializer, TransactionHistorySerializer
from .models import AccountDetails, TransactionHistory, BankDetails
from rest_framework.response import Response

user_model = get_user_model()


class AccountDetailsViewset(viewsets.ModelViewSet):

    serializer_class = AccountDetailsSerializer
    queryset = AccountDetails.objects.all()
    permission_classes = [AllowAny]
    # lookup_field = "user"
    lookup_url_kwarg = "user_id"

    def retrieve(self, request, *args, **kwargs):
        user_inst = get_user_model().objects.get(pk=kwargs["user_id"])
        acc_details_inst = AccountDetails.objects.get(user=user_inst)
        serializer = self.get_serializer(acc_details_inst)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user_inst = get_user_model().objects.get(pk=kwargs["user_id"])
        bank_id = request.data["bank_details"]
        bank_inst = BankDetails.objects.get(pk=bank_id)
        acc_details_inst = AccountDetails.objects.get(user=user_inst, bank_details=bank_inst)
        serializer = self.get_serializer(acc_details_inst, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user_inst = get_user_model().objects.get(pk=int(request.data["user"]))
        bank_id = request.data["bank_details"]
        bank_inst = BankDetails.objects.get(pk=bank_id)
        acc_details_inst = AccountDetails.objects.get(user=user_inst, bank_details=bank_inst)
        serializer = self.get_serializer(acc_details_inst, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class TransactionViewset(viewsets.ModelViewSet):
    serializer_class = TransactionHistorySerializer
    permission_classes = [AllowAny]
    queryset = TransactionHistory.objects.all()

    def retrieve(self, request, *args, **kwargs):
        user_inst = get_user_model().objects.get(pk=kwargs["user_id"])
        acc_details_inst = TransactionHistory.objects.get(user=user_inst)
        serializer = self.get_serializer(acc_details_inst)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user_inst = get_user_model().objects.get(pk=kwargs["user_id"])
        bank_id = request.data["bank_details"]
        bank_inst = BankDetails.objects.get(pk=bank_id)
        acc_details_inst = AccountDetails.objects.get(user=user_inst, bank_details=bank_inst)
        serializer = self.get_serializer(acc_details_inst, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user_inst = get_user_model().objects.get(pk=int(request.data["user"]))
        bank_id = request.data["bank_details"]
        bank_inst = BankDetails.objects.get(pk=bank_id)
        acc_details_inst = AccountDetails.objects.get(user=user_inst, bank_details=bank_inst)
        serializer = self.get_serializer(acc_details_inst, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


