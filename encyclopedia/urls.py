from django.urls import path

from . import views

#app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("newpage", views.new_page, name="newpage"),
    path("editpage/<str:name>", views.edit_page, name="editpage"),
    path("random", views.random_page, name="random"),
    path("<str:name>", views.url_entry, name="entry"),
]
