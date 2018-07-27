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
from common.object_support import assign
from common.error_support import Error
import json
import datetime
import hashlib, uuid
from manager import user_manager, event_manager, comment_manager