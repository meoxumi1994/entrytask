from common.model import LikeTab
from common.object_support import assign
import datetime, time

def create(data):
    create_time = int(time.time())
    like = LikeTab(
        user_id=data['user_id'],
        event_id=data["event_id"],
        create_time=create_time)
    like.save()

def get_by_event(data):
    likes = LikeTab.objects.filter(
        event_id=data["event_id"],
        create_time__lte=data['last_time'])[:data['limit']].values()
    return list(likes)

def get_total(data):
    likes = LikeTab.objects.filter(
        event_id=data["event_id"]).count()
    return likes

def get_by_user(data):
    likes = LikeTab.objects.filter(
        user_id=data["user_id"],
        create_time__lte=data['last_time'])[:data['limit']].values()
    return list(likes)