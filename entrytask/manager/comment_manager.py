from common.model import CategoryTab, UserTab, EventTab, CommentTab
from common.object_support import assign
import datetime, time

def get(data):
    comment = CommentTab.objects.filter(pk=data['comment_id'])
    return comment[0]

def create(data):
    create_time = int(time.time())
    comment = CommentTab(
        user_id=data['user_id'],
        event_id=data["event_id"],
        create_time=create_time)
    assign(comment, data, [ 'content' ])

    comment.save()

def get_by_event(data):
    comments = CommentTab.objects.filter(
        event_id=data["event_id"],
        create_time__lte=data['last_time'])[:data['limit']].values()
    return list(comments)