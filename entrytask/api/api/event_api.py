# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.cache import cache
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.cache import cache_page
from django.db import models
from common.model import CategoryTab, UserTab, CommentTab, EventTab, LikeTab, ParticipantTab
from common.auth import auth_visitor, get_visitor_access_token
from common.handle_support import handle_error, handle_auth_visitor, handle_json_response
from common.object_support import assign, require, get_params
from common.error_support import Error
from common.response_handle import error, success
import json
import datetime
import hashlib, uuid
from manager import event_manager

@handle_error
@handle_json_response
@handle_auth_visitor
def get_by_id(request, user_id):
    if request.method == 'GET':
        body = get_params(request)

        req = require(body, ['event_id'])
        if req:
            return error(req)

        event = event_manager.get(body)

        if not event :
            return error("can't find this event")

        return success({
            'event' : event
        })

@handle_error
@handle_json_response
@handle_auth_visitor
def search_by_tag(request, user_id):
    if request.method == 'GET':
        body = get_params(request)

        req = require(body, ['tag_name'])
        if req:
            return error(req)

        events = event_manager.search_by_tag(body)

        return success({
            'events' : events
        })

@handle_error
@handle_json_response
@handle_auth_visitor
def search(request, user_id):
    if request.method == 'GET':
        body = get_params(request)

        events = event_manager.search(body)

        return success({
            'events' : events
        })