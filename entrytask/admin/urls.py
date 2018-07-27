from django.conf.urls import url

from .api import user_api, event_api, photo_api

urlpatterns = [
    url(r'^create_admin', user_api.create_admin , name='create_admin'),
    url(r'^login_admin', user_api.login_admin, name='login_admin'),
    url(r'^create_event', event_api.create_event, name='create_event'),
    url(r'^photo', photo_api.photo, name='photo')
]