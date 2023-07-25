from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    item = models.CharField(max_length=64)


class Bid(models.Model):
    amount = models.IntegerField()


class Comment(models.Model):
    content = models.CharField()


