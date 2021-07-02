from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone

user_model = get_user_model()


class CreditCards(models.Model):
    name = models.CharField(max_length=200, blank=False)
    card_no = models.IntegerField()
    check_code = models.IntegerField()
    pin = models.IntegerField()

    class Meta:
        db_table = "credit_cards"
        verbose_name_plural = "credit_cards"


class BankDetails(models.Model):

    name = models.CharField(max_length=200)
    bank_code = models.CharField(max_length=20)
    credit_card = models.OneToOneField(
        CreditCards, on_delete=models.SET_NULL, related_name="bank_details",
        null=True,
    )

    class Meta:
        db_table = "bank_details"
        verbose_name_plural = "bank_details"


class AccountDetails(models.Model):

    user = models.ForeignKey(
        user_model, on_delete=models.SET_NULL, related_name="account_details",
        null=True
    )

    bank_details = models.ForeignKey(
        BankDetails, on_delete=models.SET_NULL, related_name="bank_details",
        null=True
    )

    account_balance = models.FloatField(blank=True, default=0.0)

    class Meta:
        db_table = "account_details"
        verbose_name_plural = "account_details"
        constraints = [
            models.constraints.UniqueConstraint(fields=["user", "bank_details"], name="user_bank")
        ]


class TransactionHistory(models.Model):
    _credit_or_debit = (
        ("CR", "CREDIT"), ("DR", "DEBIT")
    )

    user = models.ForeignKey(
        user_model, on_delete=models.SET_NULL, related_name="transaction_history",
        null=True
    )
    bank_details = models.ForeignKey(
        BankDetails, on_delete=models.SET_NULL, related_name="transaction_history",
        null=True
    )
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=2, choices=_credit_or_debit)
    date = models.DateTimeField(default=timezone.now)


# class TransactionHistoryJoin(models.Model):
#     account_details = models.ForeignKey(
#         AccountDetails, on_delete=models.SET_NULL, related_name="transaction_history_join",
#         null=True
#     )
#     transaction = models.ForeignKey(
#         TransactionHistory, on_delete=models.SET_NULL, related_name="transaction_history_join",
#         null=True
#     )

