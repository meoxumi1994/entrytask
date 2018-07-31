# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.handle_support import handle_auth_admin, handle_error, handle_json_response
from common.error_support import Error
from common.response_handle import success, error
from common.object_support import require, get_params, id_generator
import json
from manager import user_manager, event_manager


@handle_error
@handle_json_response
@handle_auth_admin
def create_event(request, admin_id):
    if request.method == 'POST' :
        body = json.loads(request.body)

        req = require(body, ['event_time'])
        if req:
            return error(req)

        body['user_id'] = admin_id

        event_manager.create(body)

        return success({})

@handle_error
@handle_json_response
@handle_auth_admin
def create_event_category(request, admin_id):
    if request.method == 'POST' :
        body = json.loads(request.body)

        req = require(body, ['event_id' , 'category_id'])
        if req:
            return error(req)

        event_manager.create_event_category(body)

        return success({})

@handle_error
@handle_json_response
@handle_auth_admin
def create_event_tag(request, admin_id):
    if request.method == 'POST' :
        body = json.loads(request.body)

        req = require(body, ['event_id' , 'tag_id'])
        if req:
            return error(req)

        event_manager.create_event_tag(body)

        return success({})