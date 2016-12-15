from django.conf.urls import url
from userprofile.views import *

urlpatterns = [
    url(r'^profile/$', user_profile),
    url(r'^profile/all$', userprofiles),
    url(r'^profile/get/(?P<userprofile_id>\d+)/$', userprofile),
    url(r'^show_profile/$', show_profile),
    url(r'^follow/(?P<userprofile_id>\d+)/$', follow),
    url(r'^show_followers/(?P<userprofile_id>\d+)/$', show_followers),
]
