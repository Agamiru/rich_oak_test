from django.contrib import admin

from .models import *


@admin.register(CreditCards)
class CreditCardAdmin(admin.ModelAdmin):
    pass


@admin.register(BankDetails)
class BankDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(AccountDetails)
class AccountDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(TransactionHistory)
class TransactionsHistoryAdmin(admin.ModelAdmin):
    pass