from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=1024)
    creation_time = models.DateTimeField('date created')
    updation_time = models.DateTimeField('date updated')
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User, related_name='likers', blank=True)
    by = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    thumbnail = models.FileField(null=True, blank=True)
    is_spam = models.BooleanField(default=False)
    by = models.ForeignKey(User, blank=True, null=True)
    downvoted_by = models.ManyToManyField(User, related_name='answers_downvoted', blank=True)
    upvoted_by = models.ManyToManyField(User, related_name='answer_upvoted', blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    answer = models.ForeignKey(Answer)
    text = models.TextField()
    comment_date = models.DateTimeField('comment date')

    def __str__(self):
        return self.text
