# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.photo_support import add_photo
from common.handle_support import handle_auth_admin, handle_error, handle_json_response
from common.error_support import Error
from common.response_handle import success, error
import json
from manager import user_manager, event_manager

@handle_error
@handle_json_response
@handle_auth_admin
def create_event(request, admin_id):
    if request.method == 'POST' :
        body = json.loads(request.body)

        if body['event_time'] is None :
            return error(Error.MISSING_EVENT_TIME)

        body['user_id'] = admin_id

        event_manager.create(body)

        return success({})