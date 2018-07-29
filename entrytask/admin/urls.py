from django.conf.urls import url

from .api import user_api, event_api, photo_api, category_api

urlpatterns = [
    url(r'^create', user_api.create_admin , name='create_admin'),
    url(r'^login', user_api.login_admin, name='login_admin'),
    url(r'^salt', user_api.get_salt, name='get_salt'),
    url(r'^get', user_api.get_admin, name='get_admin'),
    url(r'^event', event_api.create_event, name='create_event'),
    url(r'^category', category_api.get, name='category'),
    url(r'^photo', photo_api.photo, name='photo')
]