from common.model import CategoryTab, UserTab, EventTab, EventTagTab, EventCategoryTab, TagTab
from common.object_support import assign
import hashlib, uuid, datetime, time

def get(data):
    event = EventTab.objects.filter(pk=data['event_id']).values()
    if len(event) :
        event = event[0]
    else :
        event = None
    return event

def create(data):
    create_by = UserTab.objects.get(pk=data['user_id'])
    create_time = int(time.time())

    event = EventTab(create_by=create_by, create_time=create_time)
    assign(event, data, ['event_time', 'location', 'title', 'description'])
    return event.save()

def search_by_tag(data) :
    tab = TagTab.objects.filter(tag_name=data["tag_name"]).values()
    if not len(tab) :
        return None
    else :
        tab = tab[0]

    event_tags = EventTagTab.objects.filter(tag_id=tab['id']).values()

    return list(event_tags)


def search_by_category(data) :
    event_categorys = EventCategoryTab.objects.filter(category_id=data['category_id']).values()
    return list(event_categorys)


def search_by_event_time(data):
    events = EventTab.objects.filter(event_time__range=[data['start_time'], data['end_time']]).values()
    return list(events)