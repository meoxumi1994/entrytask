from common.model import ParticipantTab
from common.object_support import assign
import datetime, time

def create(data):
    create_time = int(time.time())
    participant = ParticipantTab(
        user_id=data['user_id'],
        event_id=data["event_id"],
        create_time=create_time)
    participant.save()

def get_by_event(data):
    participants = ParticipantTab.objects.filter(
        event_id=data["event_id"],
        create_time__lte=data['last_time'])[:data['limit']].values()
    return list(participants)

def get_total(data):
    participants = ParticipantTab.objects.filter(
        event_id=data["event_id"]).count()
    return participants

def get_by_user(data):
    participants = ParticipantTab.objects.filter(
        user_id=data["user_id"],
        create_time__lte=data['last_time'])[:data['limit']].values()
    return list(participants)