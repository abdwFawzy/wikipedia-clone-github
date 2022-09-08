from django.urls import path

from . import views
appname = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("EntryPage/<str:entryPage>", views.EntryPage, name="EntryPage"),
    path("EntryPage", views.SearchEntry, name="SearchEntry"),
    path("AddEntry", views.AddEntry, name="AddEntry"),
    path("editEntry/<str:entryName>", views.editEntry, name="editEntry"),
    path("randomChoice", views.randomChoice, name="randomChoice")
]
