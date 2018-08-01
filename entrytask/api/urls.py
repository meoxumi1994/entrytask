from django.conf.urls import url, include

from .api import comment_api, event_api, like_api, participant_api, user_api, photo_api

urlpatterns = [
    url(r'^create', user_api.create_visitor, name='create_visitor'),
    url(r'^login', user_api.login_visitor, name='login_visitor'),
    url(r'^salt', user_api.get_salt, name='get_salt'),
    url(r'^refresh_token', user_api.refresh_token, name='refresh_token'),
    url(r'^get', user_api.get_visitor, name='get_visitor'),

    url(r'^event_get_by_id', event_api.get_by_id, name="event_get_by_id"),
    url(r'^event_search_by_tag', event_api.search_by_tag, name="search_by_tag"),
    url(r'^event_search', event_api.search, name="event_search"),

    url(r'^comment_by_event', comment_api.get_comment_by_event, name='get_comment_by_event'),
    url(r'^comment', comment_api.create, name='create comment'),

    url(r'^like_by_event', like_api.get_like_by_event, name="get_like_by_event"),
    url(r'^like', like_api.create, name='create like'),
    url(r'^participant_by_event', participant_api.get_participant_by_event, name='participant_by_event'),
    url(r'^participant', participant_api.create, name='create participant'),

    url(r'^photo', photo_api.get_photo, name='create participant'),

]