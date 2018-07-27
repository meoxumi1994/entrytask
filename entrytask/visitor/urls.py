from django.conf.urls import url

from .api import comment_api, event_api, like_api, participant_api, user_api

urlpatterns = [
    url(r'^create_visitor', user_api.create_visitor, name='create_visitor'),
    url(r'^login_visitor', user_api.login_visitor, name='login_visitor'),
    url(r'^comment', comment_api.create, name='create comment'),
    url(r'^like', like_api.create, name='create like'),
    url(r'^participant', participant_api.create, name='create participant')
]