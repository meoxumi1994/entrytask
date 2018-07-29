# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.photo_support import add_photo
from common.handle_support import handle_auth_admin, handle_error, handle_json_response
from common.error_support import Error
from common.response_handle import success, error
import json
from manager import user_manager, event_manager, category_manager

@handle_error
@handle_json_response
@handle_auth_admin
def get(request, admin_id):
    if request.method == 'GET' :
        categories = category_manager.get_all()
        return success({
            'categories' : categories
        })