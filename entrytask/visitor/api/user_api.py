# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.cache import cache
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.cache import cache_page

from common.auth import auth_visitor, get_visitor_access_token
from common.handle_support import handle_error, handle_auth_visitor, handle_json_response
from common.error_support import Error
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

        if body['user_name'] is None or body['password'] is None:
            return {
                'status': 'error',
                'error_message': Error.USER_NAME_OR_PASSWORD
            }

        if user_manager.check_user_name_is_used(body):
            return {
                'status': 'error',
                'error_message': Error.USER_NAME_USED
            }

        user_manager.create(body)

        return {
            'status': 'success'
        }

@handle_error
@handle_json_response
def login_visitor(request):
    if request.method == 'POST' :
        body = json.loads(request.body)

        if body['user_name'] is None or body['password'] is None:
            return {
                'status': 'error',
                'error_message': Error.USER_NAME_OR_PASSWORD
            }

        body['user_type'] = 'visitor'
        user = user_manager.verify(body)

        if not user:
            return {
                'status': 'error',
                'error_message': Error.USER_NAME_OR_PASSWORD
            }

        access_token = get_visitor_access_token({
            'id': user.id,
            'user_name': user.user_name,
            'password': user.password,
            'expiration_date': (datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
        })

        return {
            'status': 'success',
            'data': {
                'access_token': access_token
            }
        }
