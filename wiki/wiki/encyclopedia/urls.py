from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.title, name="title"),
    path("editPage/<str:newTitle>", views.editPage, name="editPage"),
    path("Search", views.search, name="search"),
    path("create", views.createNewPage, name="create"),
    path("RandomPage", views.randompage, name="random"),
]
