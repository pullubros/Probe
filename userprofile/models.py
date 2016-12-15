from django.db import models
from django.contrib.auth.models import User
from question.models import Tag


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, null=True, blank=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(null=True, blank=True)
    pic = models.ImageField(default="/static/images/default.png")
    follow_tags = models.ManyToManyField("question.Tag")
    bio = models.TextField(blank=True)
    mobile = models.CharField(max_length=12, blank=True)
    college = models.CharField(max_length=1024, blank=True)
    address = models.TextField(blank=True)
    followers = models.ManyToManyField('auth.User', related_name='followers', blank=True)
    following = models.ManyToManyField('auth.User', related_name='following', blank=True)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
