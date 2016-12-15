from django.conf.urls import url
from account.views import *

urlpatterns = [
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logout),
    url(r'^loggedin/$', loggedin),
    url(r'^invalid/$', invalid_login),
    url(r'^register/$', register_user),
    url(r'^register_success/$', register_success),
]
