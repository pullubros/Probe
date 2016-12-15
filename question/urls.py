from django.conf.urls import url
from question.views import *

urlpatterns = [
    url(r'^all/$', questions),
    url(r'^tags/$', tags),
    url(r'^tag/(?P<tag_id>\d+)/$', tag),
    url(r'^get/(?P<question_id>\d+)/$', question),
    url(r'^add/$', add_question),
    url(r'^like/(?P<question_id>\d+)/$', like_question),
    url(r'^add_answer/(?P<question_id>\d+)/$', add_answer),
    url(r'^delete_answer/(?P<answer_id>\d+)/$', delete_answer),
    url(r'^upvote_answer/(?P<answer_id>\d+)/$', upvote_answer),
    url(r'^downvote_answer/(?P<answer_id>\d+)/$', downvote_answer),
    url(r'^add_comment/(?P<answer_id>\d+)/$', add_comment),
    url(r'^delete_comment/(?P<comment_id>\d+)/$', delete_comment),
    url(r'^search/$', search_title),
]
