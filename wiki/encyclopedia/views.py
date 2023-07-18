from django.shortcuts import render

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
