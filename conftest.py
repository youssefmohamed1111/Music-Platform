import pytest
from users.models import User
from knox.auth import AuthToken
from rest_framework.test import APIClient

@pytest.fixture
def auth_client(user):
    client = APIClient()
    token = AuthToken.objects.create(user=user)[1]
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    return client
@pytest.fixture
def client():
    return APIClient()