# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.photo_support import add_photo
from common.handle_support import handle_auth_admin, handle_error, handle_json_response
from common.error_support import Error
import json
from manager import user_manager, event_manager

@handle_error
@handle_json_response
@handle_auth_admin
def photo(request, admin_id):
    if request.method == 'POST' :
        body = json.loads(request.body)
        image_url = add_photo(body['base64'])
        return {
            'status': 'success'
        }