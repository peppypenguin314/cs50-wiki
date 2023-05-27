import markdown2

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def url_entry(request, name):
    mdContent = util.get_entry(name)
    if mdContent is None:
        return redirect(notFound)
    return render(request, "encyclopedia/entry.html", {
        "name": name,
        "mdContent": markdown2.markdown(mdContent)
    })
    
def search(request):
    if request.method == "POST":
        entryName = request.POST["q"]
        mdContent = util.get_entry(entryName)
        if mdContent is None:
            entries = util.list_entries()
            searchResults = []
            for entry in entries:
                if entryName in entry:
                    searchResults += [entry]
            return render(request, "encyclopedia/index.html", {
                "entries": searchResults
            })
        return render(request, "encyclopedia/entry.html", {
            "name": entryName,
            "mdContent": markdown2.markdown(mdContent)
        })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

