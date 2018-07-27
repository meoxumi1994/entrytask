from common.model import CategoryTab, UserTab, EventTab
from common.object_support import assign
import hashlib, uuid, datetime


def create(data):
    create_by = UserTab.objects.get(pk=data['user_id'])
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    event = EventTab(create_by=create_by, create_time=create_time)
    assign(event, data, ['event_time', 'location', 'title', 'description'])
    return event.save()