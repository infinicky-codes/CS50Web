from django.shortcuts import render
from markdown2 import Markdown

from . import util

markdown_converter = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    converted_html = markdown_converter.convert(util.get_entry(title))
    return render(request, "encyclopedia/wiki.html", {
        "entry": converted_html,
        "title": title
    })
