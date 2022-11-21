
import pytest
from rest_framework import status



@pytest.mark.django_db
class TestCreateRegister:
    def test_if_data_is_valid_return_201(self, auth_client):
        user_data = {"username": "admin", "email": "uif721@gmail.com",
                     "password1": "admin", "password2": "admin"}
        response = auth_client.post('/authentication/register/', user_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data == {
            "username": "admin", "email": "uif721@gmail.com"}

    def test_if_data_is_invalid_return_400(self, auth_client):
        user_data = {"username": "admin", "email": "uif721@gmail.com",
                     "password1": "admin"}
        response = auth_client.post('/authentication/register/', user_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestCreateLogin:
    def testIfDataIsValid(self, auth_client):
        user_data = {"username": "admin", "email": "uif721@gmail.com",
                     "password1": "admin", "password2": "admin"}
        auth_client.post(
            '/authentication/register/', user_data)
        response = auth_client.post(
            '/authentication/login/', {"username": "admin", "password": "admin"})
        assert response.status_code == status.HTTP_200_OK

    def testIfDataIsInvalid(self, auth_client):
        user_data = {"username": "admin", "email": "uif721@gmail.com",
                     "password1": "admin", "password2": "admin"}
        auth_client.post(
            '/authentication/register/', user_data)
        response = auth_client.post('/authentication/login/',
                                    {"username": "admin"})
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestCreateLogout:
    def testIfNoContent(self, auth_client):
        response = auth_client.post('/authentication/logout/')
        assert response.status_code == status.HTTP_204_NO_CONTENT_client.get('/artists/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data == [
            {'id': artist.id, 'stageName': artist.stageName,
                'socialLinkField': artist.socialLinkField}]

   