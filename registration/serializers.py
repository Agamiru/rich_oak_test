from rest_framework import serializers


from .models import User


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        exclude = ["password"]
        read_only_fields = [
            "id", "last_login", "is_superuser", "is_staff", "is_active",
            "groups", "user_permissions"
        ]

