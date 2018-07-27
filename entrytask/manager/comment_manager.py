from common.model import CategoryTab, UserTab, EventTab, CommentTab
from common.object_support import assign
import datetime

def create(data):
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    comment = CommentTab(
        user_id=data['user_id'],
        event_id=data["event_id"],
        create_time=create_time)
    assign(comment, data, [ 'content' ])
    comment.save()