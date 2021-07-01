from datetime import timedelta

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import get_user_model

from rest_framework import routers as r

from rest_framework_simplejwt import settings as jwt_settings


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from registration.views import UserViewSet
from finances.views import AccountDetailsViewset


user_model = get_user_model()

jwt_settings.DEFAULTS["ACCESS_TOKEN_LIFETIME"] = timedelta(days=7)
jwt_settings.DEFAULTS["USER_ID_FIELD"] = user_model.USERNAME_FIELD

router = r.SimpleRouter()
router.register("user", UserViewSet)
router.register("accounts", AccountDetailsViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', include("registration.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += router.urls
