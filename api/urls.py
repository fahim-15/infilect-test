from django.conf.urls import url
from django.urls import re_path
from rest_framework.authtoken import views

from media_mgmt.views import user_group, user_group_photos
from user_mgmt.views import logout

urlpatterns = [
    url(r'^(?P<version>(v1))/login/$',
        views.obtain_auth_token
    ),
    url(r'^(?P<version>(v1))/logout/$',
        logout
    ),
    re_path(
        r'^(?P<version>(v1))/groups/$',
        user_group
    ),
    re_path(
        r'^(?P<version>(v1))/group/(?P<group_id>[0-9]+)/$',
        user_group
    ),
    re_path(
        r'^(?P<version>(v1))/photos/(?P<photo_id>[0-9]+)/$',
        user_group_photos
    ),
    re_path(
        r'^(?P<version>(v1))/photos/$',
        user_group_photos
    ),
]
