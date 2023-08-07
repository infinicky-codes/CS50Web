from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=64)


class Listing(models.Model):
    # Each listing is created by one specific User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # and has a title, description and current price
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255, default='')
    # TODO: get last (= highest) bid
    current_price = models.DecimalField(max_digits=7, decimal_places=2)
    # optional fields
    image_url = models.CharField(max_length=255, default='')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.id}: {self.title}, €{self.current_price}"


class Bid(models.Model):
    # Each bid is on one specific Listing
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    # made by one specific User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # and is for a certain amount
    # TODO: new bid must be higher than last bid on same listing
    amount = models.DecimalField(max_digits=7, decimal_places=2)


class Comment(models.Model):
    # Each comment is on one specific Listing
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    # made by one specific User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

