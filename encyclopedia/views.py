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
    

