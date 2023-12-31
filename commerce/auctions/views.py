from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Category


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def create(request):
    if request.method == "POST":
        user = request.user
        title = request.POST["title"]
        desc = request.POST["description"]
        price = request.POST["price"]
        bid = None
        url = request.POST.get("image_url", None)
        cat = request.POST.get("category", None)

        listing = Listing(user = user, title = title, 
                    description = desc, asking_price = price,
                    highest_bid = bid, image_url = url, category = cat)
        listing.save()
        return render(request, "auctions/index.html", {
            "listings": Listing.objects.all()
        })
    
    else:
        return render(request, "auctions/create.html", {
            "categories": Category.objects.all()
        })


def watchlist(request):
    return render(request, "auctions/create.html")


def categories(request):
    return render(request, "auctions/create.html")


### User specific Views ###

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
