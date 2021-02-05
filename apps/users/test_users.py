import pytest
from django.test import Client
from .models import User


@pytest.mark.django_db
class TestCustomUserManager:
    superuser_params = {
        "email": "test@superuser.com",
        "first_name": "John",
        "last_name": "Snow",
        "password": "test_password",
    }

    def test_create_user(self):
        new_user = User.objects.create_user(email="test@user.com")
        user = User.objects.first()
        assert new_user == user

    def test_str(self):
        user = User.objects.create_user(email="test@user.com")
        assert str(user) == "test@user.com"

    def test_create_superuser(self):
        new_superuser = User.objects.create_superuser(**self.superuser_params)
        user = User.objects.first()
        assert new_superuser == user
        assert user.is_superuser
        assert user.first_name == "John"
        assert user.last_name == "Snow"

    @pytest.mark.parametrize(
        "is_staff, is_superuser", [(False, False), (False, True), (True, False)]
    )
    def test_create_superuser_failure(self, is_staff, is_superuser):
        with pytest.raises(ValueError):
            User.objects.create_superuser(
                **self.superuser_params,
                is_staff=is_staff,
                is_superuser=is_superuser,
            )


class TestDjangoLoginRedirectTest:
    def test_login(self):
        c = Client()
        response = c.get("/login")
        assert response.status_code == 301
