# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.handle_support import handle_error, handle_auth_visitor, handle_json_response
from common.object_support import assign, require, get_params
from common.response_handle import error, success
from common.error_support import Error
import json
from manager import user_manager, event_manager, participant_manager

@handle_error
@handle_json_response
@handle_auth_visitor
def create(request, user_id):
    if request.method == 'POST' :
        body = json.loads(request.body)
        body['user_id'] = user_id

        participant_manager.create(body)
        return success({})


@handle_error
@handle_json_response
@handle_auth_visitor
def get_participant_by_event(request, user_id):
    if request.method == 'GET' :
        body = get_params(request)

        req = require(body, ['last_time', 'event_id', 'limit'])
        if req :
            return error(req)

        participants = participant_manager.get_by_event(body)

        return success({
            'participants' : participants
        })

@handle_error
@handle_json_response
@handle_auth_visitor
def get_participant_by_user(request, user_id):
    if request.method == 'POST' :
        body = json.loads(request.body)

        body['user_id'] = user_id
        req = require(body, ['last_time', 'limit'])
        if req :
            return error(req)

        participants = participant_manager.get_by_user(body)

        return success({
            'participants' : participants
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

        total_participant = participant_manager.get_total(body)

        return success({
            'total_participant' : total_participant
        })
