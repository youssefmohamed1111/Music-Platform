
import pytest
from rest_framework import status


@pytest.mark.django_db
class TestCreateArtist:
    def testIfArtistsAreFound(self, auth_client, artists):
        response = auth_client.get('/artists/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data == [
            {'id': artists.id, 'stageName': artists.stageName,
                'socialLinkField': artist.socialLinkField}]

    def testIfArtistisFound(self, auth_client, artists):
        response = auth_client.get(f'/artists/{artists.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data == [
            {'id': artists.id, 'stageName': artists.stageName,
                'socialLinkField': artists.socialLinkField}]