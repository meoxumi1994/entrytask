# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.model import CategoryTab, UserTab, CommentTab, EventTab, LikeTab, ParticipantTab
from common.handle_support import handle_error, handle_auth_visitor, handle_json_response
from common.object_support import assign, require, get_params
from common.error_support import Error
from common.response_handle import error, success
import json
import datetime
from manager import user_manager, event_manager, comment_manager

@handle_error
@handle_json_response
@handle_auth_visitor
def create(request, user_id):
    if request.method == 'POST' :
        body = json.loads(request.body)

        req = require(body, ['content', 'event_id'])
        if req:
            return error(req)

        body['user_id'] = user_id

        comment_manager.create(body)
        return success({})


@handle_error
@handle_json_response
@handle_auth_visitor
def get_comment_by_event(request, user_id):
    if request.method == 'GET' :
        body = get_params(request)

        req = require(body, ['last_time', 'event_id', 'limit'])
        if req :
            return error(req)

        comments = comment_manager.get_by_event(body)

        return success({
            'comments' : comments
        })

@handle_error
@handle_json_response
@handle_auth_visitor
def get_comment_by_user(request, user_id):
    if request.method == 'POST' :
        body = json.loads(request.body)

        body['user_id'] = user_id
        req = require(body, ['last_time', 'limit'])
        if req :
            return error(req)

        comments = comment_manager.get_by_user(body)

        return success({
            'comments' : comments
        })