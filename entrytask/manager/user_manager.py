from common.model import CategoryTab, UserTab, EventTab
from common.object_support import assign
import hashlib, uuid, datetime


def create(data):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(data['password'] + salt).hexdigest()
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = UserTab(password=hashed_password, create_time=create_time, salt=salt, user_type=data['user_type'])
    assign(user, data, ['user_name', 'email', 'address'])
    return user.save()

def check_user_name_is_used(data):
    return UserTab.objects.filter(user_name=data['user_name'], user_type=data['user_type'])

def get_salt(data):
    user = UserTab.objects.filter(user_name=data['user_name'], user_type=data['user_type'])
    if not user:
        return None
    return user[0].salt

def verify(data):
    user = UserTab.objects.filter(user_name=data['user_name'], user_type=data['user_type'])
    if not user:
        return None
    hashed_password = hashlib.sha512(data['password'] + user[0].salt).hexdigest()
    if hashed_password != user[0].password:
        return None
    return user[0]