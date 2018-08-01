from common.model import PhotoTab
from common.object_support import assign
import datetime, time

def get_by_event(data):
    photos = PhotoTab.objects.filter(
        event_id=data["event_id"]).values()
    return list(photos)