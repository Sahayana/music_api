from django.test import TestCase
from music.services.track_service import get_a_track, get_list_track
from music.models.track import Track
from datetime import datetime


class TestTrackService(TestCase):

    def test_get_a_single_track(self) -> None:
        # Given
        track = Track.objects.create(title='test_title', artist='test_artist', duration=100, last_play=datetime.now())
        
        # When
        result_track = get_a_track(track_id=track.id)

        # Then
        self.assertIsNotNone(track.id)
        self.assertIsNotNone(result_track)
        self.assertEqual(track.id, result_track.id)
        self.assertEqual('test_title', result_track.title)

    def test_get_list_track(self) -> None:
        
        # Given
        tracks = [Track.objects.create(title=f'test_title#{i}', artist=f'test_artist#{i}', duration=100, last_play=datetime.now()) for i in range(1,11)]

        # When
        result_tracks = get_list_track(offset=0, limit=10)

        # Then
        self.assertEqual(len(tracks), len(result_tracks))
        self.assertEqual([track.id for track in tracks], [track.id for track in result_tracks])
        