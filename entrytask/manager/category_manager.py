from common.model import CategoryTab
from common.object_support import assign
import datetime, json

def get_all():
    categories = list(CategoryTab.objects.all().values())
    return categories