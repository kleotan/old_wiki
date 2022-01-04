from django.urls import path
from django.urls import path
from . import views
from django.conf.urls import url

app_name ="encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.get_convert, name="convert"),
    path('/', views.search, name="search"),
    path("new_art/", views.add_entry, name="new_art"),
    path('edit/<str:title>', views.edit, name="edit"),
    path("saveEdit/", views.saveEdit, name="saveEdit"),
    path("random/", views.random_page, name="random")
           
]

