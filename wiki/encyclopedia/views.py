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
    If the query matches the name of an encyclopedia entry, the user
    will be redirected to that entry's page. If not, the user is 
    taken to a search results page that displays a list of all 
    encyclopedia entries that have the query as a substring.
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
    
    if len(search_results) == 0:
        empty = True
    
    # Return list of search results
    return render(request, "encyclopedia/search_results.html", {
        "results": search_results,
        "empty": empty
    }) 


def create(request):
    """
    Loads the Create New Page page, or when saving a new wiki,
    saves it to disk and loads newly created page.
    """
    # Create new wiki if saved
    if request.method == "POST":
        form = CreateWikiForm(request.POST)
        # Server-side validation
        if form.is_valid():
            return add_wiki(request, form)
        else:
            return render(request, "encyclopedia/create_wiki.html", {
                "form": form
            })

    # Just load the Create New Page page
    return render(request, "encyclopedia/create_wiki.html", {
            "form": CreateWikiForm()
    })


def add_wiki(request, form):
    title = form.cleaned_data["title"]
    # Check if a page with this title already exists 
    if util.get_entry(title) != None:
        return render(request, "encyclopedia/create_wiki.html", {
            "form": form,
            "message": "A page with this title already exists."
        })        
    # Save new wiki and load newly created page
    else:
        content = form.cleaned_data["content"]
        util.save_entry(title, content)
        return wiki(request, title)


# TODO: figure out how to get the title parameter in here
def edit(request, title):
    """
    Changes the content of an encyclopedia entry and loads the newly
    edited page.
    """
    # Update the entry
    if request.method == "POST":
        form = EditWikiForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
        return wiki(request, title)

    # Load the Edit Page page
    form = EditWikiForm()
    original_text = util.get_entry(title)
    form.fields['content'].initial = original_text
    return render(request, "encyclopedia/edit_wiki.html", {
        "form": form,
        "title": title
    })


class CreateWikiForm(forms.Form):
    # Client-side validation
    title = forms.CharField(label="Title", required=True) 
    content = forms.CharField(label="Content", 
                              widget=forms.Textarea())


class EditWikiForm(forms.Form):
    content = forms.CharField(label="Edit Content", 
                              widget=forms.Textarea())  
