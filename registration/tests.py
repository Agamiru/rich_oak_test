from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from finances.models import BankDetails, AccountDetails







class TestApi(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.user_model = get_user_model()


    def test_create(self):
        user_data = {
            "email": "chidi@gmail.com", "first_name": "Chidi",
            "last_name": "Nnadi", "password": "agamiru"
        }

        user_inst = self.user_model.objects.create(**user_data)

        bank_det_data = {"name": "GTB", "bank_code": "37809"}
        bank_det_inst = BankDetails.objects.create(**bank_det_data)

        acc_det_data = {
            "user": user_inst, "bank_details": bank_det_inst,
            # "bvn": "374930348",
        }

        acc_raw_values = {
            "user": f"{user_inst.pk}", "bank_details": f"{bank_det_inst.pk}",
            # "bvn": "374930348",
        }
        acc_det_inst = AccountDetails.objects.create(**acc_det_data)
        # res = self.client.patch(f"/user/{user_inst.id}/", data={"id": "8"}, content_type="application/json")
        # print(res.data)
        res = self.client.post(f"/accounts/", data=acc_raw_values, content_type="application/json")
        print(res.data)


