import jwt
import json
import traceback
import datetime
from collections import namedtuple
from common.config import Config

def get_admin_access_token(data):
    return jwt.encode(data, Config.SECRET_KEY_ADMIN , algorithm='HS256')

def get_visitor_access_token(data):
    return jwt.encode(data, Config.SECRET_KEY_VISITOR , algorithm='HS256')

def auth_visitor(request):
    try:
        access_token = request.META["HTTP_ENTRY_TASK_TOKEN"]
        data_json = jwt.decode(access_token, Config.SECRET_KEY_VISITOR, algorithms=['HS256'])
        data = json.loads(json.dumps(data_json))
        if data['id'] and datetime.datetime.strptime(data['expiration_date'], "%Y-%m-%d %H:%M:%S") >= datetime.datetime.now() :
            return data['id']
    except:
        return False
    return False

def auth_admin(request):
    try:
        access_token = request.META["HTTP_ENTRY_TASK_TOKEN"]
        data_json = jwt.decode(access_token, Config.SECRET_KEY_ADMIN, algorithms=['HS256'])
        data = json.loads(json.dumps(data_json))
        if data['id'] :
            return data['id']
    except:
        return False
    return False


__All__ = []