from django.db import models

from django.contrib.auth import get_user_model



user_model = get_user_model()

class FinanceManager(models.Manager):


    def credit_account(self, user_inst, credit_amnt):
        acc_det_inst = self.get_acc_det_inst(user_inst)
        new_bal = acc_det_inst.account_balane


    def get_acc_det_inst(self, user_inst):
        return self.get(user=user_inst)




