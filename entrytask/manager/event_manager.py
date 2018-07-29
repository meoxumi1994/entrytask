from common.model import CategoryTab, UserTab, EventTab, EventTagTab, EventCategoryTab
from common.object_support import assign
import hashlib, uuid, datetime


def get(data):
    event = EventTab.objects.filter(pk=data['event_id'])
    return event[0]

def create(data):
    create_by = UserTab.objects.get(pk=data['user_id'])
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    event = EventTab(create_by=create_by, create_time=create_time)
    assign(event, data, ['event_time', 'location', 'title', 'description'])
    return event.save()

def search_by_tag(data):
    events = EventTagTab.objects.extra(where=["%s LIKE postcode_prefix||'%%'"],
                                     param=[data['tag_prefix_string']])
    return events

def search_by_category(data):
    events = EventCategoryTab.objects.filter(category_id=data['category_id'])
    return events

def search_by_event_time(data):
    events = EventTab.objects.filter(
        event_time__level__gte=data['start_time'],
        event_time__level__lte=data['end_time'])
    return events