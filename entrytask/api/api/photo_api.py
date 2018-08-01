from __future__ import unicode_literals

from django.core.cache import cache
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.cache import cache_page

from common.auth import auth_visitor, get_visitor_access_token
from common.handle_support import handle_error, handle_auth_visitor, handle_json_response
from common.error_support import Error
from common.response_handle import error, success
from common.object_support import require, get_params
import json
import datetime
from manager import photo_manager

@handle_error
@handle_json_response
@handle_auth_visitor
def get_photo(request, user_id):
    if request.method == 'GET':
        body = get_params(request)

        req = require(body, ['event_id'])
        if req:
            return error(req)

        photo = photo_manager.get_by_event(body)

        if not photo :
            return error("can't find photos for this event")

        return success({
            'photo' : photo
        })
