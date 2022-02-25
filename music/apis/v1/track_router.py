from typing import Dict, List, Tuple

from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import File, Router, UploadedFile
from ninja.errors import HttpError

from music.apis.v1.schemas.track_response import TrackResponse, UploadResponse
from music.models.track import Track
from music.services.track_service import get_a_track, get_list_track, upload_file

router = Router(tags=["Track"])


@router.get("/{track_id}", response={200: TrackResponse})
def get_single_track(request: HttpRequest, track_id: int) -> Tuple[int, Track]:
    try:
        track = get_a_track(track_id=track_id)
    except Track.DoesNotExist:
        raise HttpError(404, f"#{track.title} Not Found.")

    return 200, track


@router.get("/", response={200: List[TrackResponse]})
def get_tracks(request: HttpRequest, offset: int = 0, limit: int = 10) -> Tuple[int, QuerySet[Track]]:
    tracks = get_list_track(offset=offset, limit=limit)
    return 200, tracks


@router.post("/", url_name="upload", response={201: UploadResponse})
def upload_image(request: HttpRequest, file: UploadedFile = File(...)) -> Tuple[int, Dict]:
    data = upload_file(uploaded_file=file)
    return 201, data
