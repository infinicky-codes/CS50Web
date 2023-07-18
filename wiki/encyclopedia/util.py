import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


from markdown2 import Markdown

markdown_converter = Markdown()


def list_entries():
    """
    Returns a sorted list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    filename = f"entries/{title}.md"
    try:
        f = default_storage.open(filename)
        decoded_file = f.read().decode("utf-8")
        return decoded_file
    except FileNotFoundError:
        # return "The requested page could not be found"
        return None


def convert_file(file):
        """ 
        Converts a Markdown file to an HTML file.
        """
        return markdown_converter.convert(file)

