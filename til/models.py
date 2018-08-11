from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    created_date = models.DateTimeField(default=timezone.localtime(timezone.now()))
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Til(models.Model):
    id = models.AutoField(primary_key=True)
    til_item = models.CharField(max_length=500,  default="")
    created_date = models.DateTimeField(default=timezone.localtime(timezone.now()))
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    plan_item = models.CharField(max_length=500,  default="")
    created_date = models.DateTimeField(default=timezone.localtime(timezone.now()))
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    review_item = models.CharField(max_length=500,  default="")
    created_date = models.DateTimeField(default=timezone.localtime(timezone.now()))
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
