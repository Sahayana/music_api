

from django.db.models import QuerySet
from ninja import File
from ninja.files import UploadedFile

from music.models.track import Track


def get_a_track(track_id: int) -> Track:
    track = Track.objects.filter(id=track_id).get()
    return track


def get_list_track(offset: int, limit: int) -> QuerySet[Track]:
    return Track.objects.all()[offset : offset + limit]


def upload_file(uploaded_file: UploadedFile = File(...)) -> dict:
    file = uploaded_file.read().decode()

    data = {
        "name": uploaded_file.name,
        "length": len(file),
        "file": file,
    }

    return data
