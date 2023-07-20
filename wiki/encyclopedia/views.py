from django.shortcuts import render
from django import forms
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, title):
    # Get correct entry file
    entry = util.get_entry(title)

    # Convert to HTML, or use an error message
    html = "<h1 id=\"notfound\">The requested page could not be found.</h1>"
    if entry != None:
        html = util.convert_file(entry)

    return render(request, "encyclopedia/wiki.html", {
        "entry": html,
        "title": title
    })


def search(request):
    """
    If the query matches the name of an encyclopedia entry, the user will 
    be redirected to that entry's page.
    If not, the user is taken to a search results page that displays 
    a list of all encyclopedia entries that have the query as a substring.
    """
    search_results = []
    query = request.GET.get("q").lower()
    # If existing entry, go to that page
    for entry in util.list_entries():
        entry_lower = entry.lower()
        if query == entry_lower:
            return wiki(request, query)
        # If text matches entry, add to search results
        elif query in entry_lower:
            search_results.append(entry)
    
    # Return list of search results
    return render(request, "encyclopedia/search_results.html", {
        "results": search_results
    }) 


def create(request):
    return render(request, "encyclopedia/create_wiki.html", {
        "form": CreateWikiForm()
    })

    if request.method == "post":
        form = CreateWikiForm(request.POST)
        # check validity? need title and content
        title = form.cleaned_data["Title"]
        content = form.cleaned_data["Content"]
        # add wiki to entries
        util.save_entry(title, content)

    else:
        return render(request, "encyclopedia/create_wiki.html")


class CreateWikiForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")
