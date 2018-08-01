from common.model import CategoryTab, UserTab, EventTab
from common.object_support import assign
import hashlib, uuid, datetime, json, time
from django.core.cache import cache

cache.clear()

def get(data):
    if cache.has_key(data['user_id']) :
        return cache.get(data['user_id'])
    user = UserTab.objects.filter(pk=data['user_id']).values()
    if len(user) :
        user = user[0]
    else:
        user = None
    cache.set(data['user_id'], user)
    return user

def create_5000():
    for i in range(5010):
        user_name = "user" + str(i) + "@gmail.com"
        create_time = int(time.time())
        user = UserTab(password="f78dsaf78sad7g8dsa7g897sf89dsa7g8adf78as97f8sa97f89sad7f",
                       create_time=create_time, salt="ad7g8dsa7g897sf89ds",
                       user_type='visitor',
                       user_name=user_name,
                       email=user_name,
                       address="hanoi , cau giay"
                       )
        user.save()

def create(data):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(data['password'] + salt).hexdigest()
    create_time = int(time.time())
    user = UserTab(password=hashed_password, create_time=create_time, salt=salt, user_type=data['user_type'])
    assign(user, data, ['user_name', 'email', 'address'])

    # cache.set(data['user_name'], user)
    return user.save()

def check_user_name_is_used(data):
    # if cache.has_key(data['user_name']) :
    #     return cache.get(data['user_name'])

    user = UserTab.objects.filter(user_name=data['user_name'], user_type=data['user_type']).values()
    if len(user) :
        user = user[0]
    else:
        user = None

    # cache.set(data['user_name'], user)
    return user

def get_salt(data):
    if cache.has_key(data['user_name']) :
        val = cache.get(data['user_name'])
        if not val:
            return None
        return val['salt']

    user = UserTab.objects.filter(user_name=data['user_name'], user_type=data['user_type']).values()
    if len(user) :
        user = user[0]
    else:
        user = None

    cache.set(data['user_name'], user)

    if not user:
        return None
    return user['salt']

def verify(data):

    # if cache.has_key(data['user_name']) :
    #     val = cache.get(data['user_name'])
    #     if not val:
    #         return None
    #     return val

    user = UserTab.objects.filter(user_name=data['user_name']).values()
    if len(user) :
        user = user[0]
    else:
        user = None

    # cache.set(data['user_name'], user)

    if not user:
        return None

    if data['password'] != user['password']:
        return None
    return user