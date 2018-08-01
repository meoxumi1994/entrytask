# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.auth import auth_visitor, get_visitor_access_token
from common.handle_support import handle_error, handle_auth_visitor, handle_json_response
from common.error_support import Error
from common.response_handle import error, success
from common.object_support import require, get_params
import json
import datetime
from manager import user_manager, event_manager, comment_manager

# Create API below
@handle_error
@handle_json_response
def create_visitor(request):
    if request.method == 'POST' :
        body = json.loads(request.body)
        body['user_type'] = 'visitor'

        req = require(body, ['user_name', 'password'])
        if req:
            return error(req)

        if user_manager.check_user_name_is_used(body):
            return error(Error.USER_NAME_USED)

        user_manager.create(body)

        return success({})

@handle_error
@handle_json_response
def get_salt(request):
    if request.method == 'GET' :
        body = get_params(request)

        req = require(body, ['user_name'])
        if req:
            return error(req)

        body['user_type'] = 'visitor'
        salt = user_manager.get_salt(body)

        return success({ 'salt': salt })

@handle_error
@handle_json_response
def login_visitor(request):
    if request.method == 'POST' :
        body = json.loads(request.body)

        req = require(body, ['user_name', 'password'])
        if req:
            return error(req)

        body['user_type'] = 'visitor'
        user = user_manager.verify(body)

        if not user:
            return error(Error.WRONG_USER_NAME_OR_PASSWORD)

        access_token = get_visitor_access_token({
            'id': user['id'],
            'user_name': user['user_name'],
            'password': user['password'],
            'expiration_date': (datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
        })

        return success({
                'access_token': access_token
            })

@handle_error
@handle_json_response
@handle_auth_visitor
def get_visitor(request, user_id):
    if request.method == 'GET':
        body = get_params(request)

        req = require(body, ['user_id'])
        if req:
            return error(req)

        user = user_manager.get(body)

        if not user :
            return error("can't find this event")

        return success({
            'user' : user
        })


