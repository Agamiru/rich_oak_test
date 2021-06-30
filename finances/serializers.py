from rest_framework import serializers


from .models import BankDetails, AccountDetails, TransactionHistory
from registration.serializers import UserSerializer


class BankDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankDetails
        fields = "__all__"


class AccountDetailsSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    bank_details = BankDetailsSerializer(read_only=True)

    class Meta:
        model = AccountDetails
        fields = "__all__"
        read_only_fields = ["account_balance"]


class TransactionHistorySerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = TransactionHistory
        fields = "__all__"
