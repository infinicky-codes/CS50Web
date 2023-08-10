from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"Category {self.id}: {self.title}"


# TODO: get last (= highest) bid to populate current_price,
#       or current_price = asking_price?
#       Maybe name change is in order: highest_bid
class Listing(models.Model):
    # Each listing is created by one specific User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255, default='')
    asking_price = models.DecimalField(max_digits=7, decimal_places=2)
    # optional fields
    current_price = models.DecimalField(max_digits=7, decimal_places=2, 
                                        null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    # A listing can belong to only 1 category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                 null=True, blank=True)

    def __str__(self):
        if self.current_price == None:
            self.current_price = self.asking_price
        return f"Listing #{self.id}: {self.title}, €{self.current_price}"


# TODO: user can't bid on own listing
# TODO: new bid must be higher than listing.current_price
class Bid(models.Model):
    # Each bid is on one specific Listing
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,
                                related_name="bids")
    # made by one specific User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"Bid #{self.id}: €{self.amount} on {self.listing.title}"


class Comment(models.Model):
    # Each comment is on one specific Listing
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, 
                                related_name="comments")
    # made by one specific User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __str__(self):
        return f"Comment (ID #{self.id}) on {self.listing.title} by User: {self.user}"