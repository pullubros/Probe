from django.contrib import admin
from question.models import Question, Tag, Answer, Comment

# Register your models here.
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
