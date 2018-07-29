from common.model import LikeTab
from common.object_support import assign
import datetime

def create(data):
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    like = LikeTab(
        user_id=data['user_id'],
        event_id=data["event_id"],
        create_time=create_time)
    like.save()

def get_by_event(data):
    likes = LikeTab.objects.filter(
        event_id=data["event_id"],
        create_time__level__lte=data['last_time'])[:data['limit']]
    return likes

def get_total(data):
    likes = LikeTab.objects.filter(
        event_id=data["event_id"]).count()
    return likes

def get_by_user(data):
    likes = LikeTab.objects.filter(
        user_id=data["user_id"],
        create_time__level__lte=data['last_time'])[:data['limit']]
    return likes