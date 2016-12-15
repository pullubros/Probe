from django.conf.urls import url
from notification.views import *

urlpatterns = [
    url(r'^show/(?P<notification_id>\d+)/$', show_notification),
    url(r'^delete/(?P<notification_id>\d+)/$', delete_notification),
]
