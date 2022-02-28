from django.test import TestCase
from music.services.track_service import get_a_track
from music.models.track import Track
from datetime import datetime



class TestTrackRouter(TestCase):

    def test_response_get_a_single_track(self) -> None:
        # Given        
        track = Track.objects.create(title='test_title!!', artist='test_artist!!', duration=100, last_play=datetime.now())

        # When        
        response = self.client.get(f'/api/v1/tracks/{track.id}')

        # Then        
        self.assertEqual(200, response.status_code)
        