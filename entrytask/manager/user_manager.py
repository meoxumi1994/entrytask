from common.model import CategoryTab, UserTab, EventTab
from common.object_support import assign
import hashlib, uuid, datetime, json
from django.core.cache import cache

def get(data):
    if cache.has_key(data['user_name']) :
        val = cache.get(data['user_name'])
        if not val:
            return None
        return val.values()[0]

    user = UserTab.objects.filter(pk=data['user_id'])
    cache.set(data['user_id'], user)
    return user.values()[0]

def create(data):

    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(data['password'] + salt).hexdigest()
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = UserTab(password=hashed_password, create_time=create_time, salt=salt, user_type=data['user_type'])
    assign(user, data, ['user_name', 'email', 'address'])

    cache.set(data['user_name'], user)
    return user.save()

def check_user_name_is_used(data):
    if cache.has_key(data['user_name']) :
        val = cache.get(data['user_name'])
        if not val:
            return None
        return val

    user = UserTab.objects.filter(user_name=data['user_name'], user_type=data['user_type'])

    cache.set(data['user_name'], user)
    return user

def get_salt(data):
    if cache.has_key(data['user_name']) :
        val = cache.get(data['user_name'])
        if not val:
            return None
        return val.values()[0].salt

    user = UserTab.objects.filter(user_name=data['user_name'], user_type=data['user_type'])
    cache.set(data['user_name'], user)

    if not user:
        return None
    return user[0].salt

def verify(data):

    if cache.has_key(data['user_name']) :
        val = cache.get(data['user_name'])
        if not val:
            return None
        return val.values()[0]

    user = UserTab.objects.filter(user_name=data['user_name'], user_type=data['user_type'])
    cache.set(data['user_name'], user)

    if not user:
        return None
    hashed_password = hashlib.sha512(data['password'] + user[0].salt).hexdigest()


    if data['password'] != user[0].password:
        return None
    return user.values()[0]