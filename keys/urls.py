from django.urls import path
from . import views

app_name = "keys"
urlpatterns = [
    path("", views.ItemListView.as_view(), name="list_items"),
    path("create/", views.ItemCreateView.as_view(), name="create_items")
]
