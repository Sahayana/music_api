from datetime import datetime

from ninja import Schema


class TrackResponse(Schema):

    title: str
    artist: str
    duration: float
    last_play: datetime

class UploadResponse(Schema):
    
    name: str
    length: int
    file: str