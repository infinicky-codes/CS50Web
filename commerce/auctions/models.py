from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    # Each listing is created by one specific User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=64)
    asking_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.id}: {self.item_name}, €{self.asking_price}"


class Bid(models.Model):
    # Each bid is on one specific Listing
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    # made by one specific User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # and is for a certain amount
    amount = models.DecimalField(max_digits=7, decimal_places=2)


class Comment(models.Model):
    # Each comment is on one specific Listing
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    # made by one specific User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # and has a content of maximum 256 characters
    content = models.CharField(max_length=256)
    


