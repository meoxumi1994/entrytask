# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.model import CategoryTab, UserTab, CommentTab, EventTab, LikeTab, ParticipantTab
from common.auth import auth_visitor, get_visitor_access_token
from common.handle_support import handle_error, handle_auth_visitor, handle_json_response
from common.object_support import assign
from common.error_support import Error
import json
import datetime
from manager import user_manager, event_manager, comment_manager

@handle_error
@handle_json_response
@handle_auth_visitor
def create(request, user_id):
    if request.method == 'POST' :
        body = json.loads(request.body)
        body['user_id'] = user_id

        comment_manager.create(body)
        return {
            'status': 'success'
        }


@handle_error
@handle_json_response
@handle_auth_visitor
def get_comment_by_event(request, user_id):
    if request.method == 'POST' :
        body = json.loads(request.body)
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment = CommentTab(
            user_id=user_id,
            event_id=body["event_id"],
            create_time=create_time)
        assign(comment, json.loads(request.body), [ 'content' ])
        comment.save()
        return {
            'status': 'success'
        }