# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.handle_support import handle_error, handle_auth_visitor, handle_json_response
from common.object_support import assign, require
from common.response_handle import error, success
from common.error_support import Error
import json
from manager import user_manager, event_manager, like_manager

@handle_error
@handle_json_response
@handle_auth_visitor
def create(request, user_id):
    if request.method == 'POST' :
        body = json.loads(request.body)

        req = require(body, ['user_id'])
        if req:
            return error(req)

        body['user_id'] = user_id

        like_manager.create(body)
        return success({})


@handle_error
@handle_json_response
@handle_auth_visitor
def get_like_by_event(request, user_id):
    if request.method == 'POST' :
        body = json.loads(request.body)

        req = require(body, ['last_time', 'event_id', 'limit'])
        if req :
            return error(req)

        likes = like_manager.get_by_event(body)

        return success({
            'likes' : likes
        })

@handle_error
@handle_json_response
@handle_auth_visitor
def get_like_by_user(request, user_id):
    if request.method == 'POST' :
        body = json.loads(request.body)

        body['user_id'] = user_id
        req = require(body, ['last_time', 'limit'])
        if req :
            return error(req)

        likes = like_manager.get_by_user(body)

        return success({
            'likes' : likes
        })

@handle_error
@handle_json_response
@handle_auth_visitor
def get_total(request, user_id):
    if request.method == 'POST' :
        body = json.loads(request.body)

        req = require(body, ['event_id'])
        if req :
            return error(req)

        total_like = like_manager.get_total(body)

        return success({
            'total_like' : total_like
        })
