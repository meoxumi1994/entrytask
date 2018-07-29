from common.model import CategoryTab, UserTab, EventTab, CommentTab
from common.object_support import assign
import datetime

def get(data):
    comment = CommentTab.objects.filter(pk=data['comment_id'])
    return comment[0]

def create(data):
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    comment = CommentTab(
        user_id=data['user_id'],
        event_id=data["event_id"],
        create_time=create_time)
    assign(comment, data, [ 'content' ])
    comment.save()

def get_by_event(data):
    comments = CommentTab.objects.filter(
        event_id=data["event_id"],
        create_time__level__lte=data['last_time'])[:data['limit']]
    return comments

def get_by_user(data):
    comments = CommentTab.objects.filter(
        user_id=data["user_id"],
        create_time__level__lte=data['last_time'])[:data['limit']]
    return comments