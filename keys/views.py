from django.shortcuts import render
from django.views.generic import CreateView, ListView
from keys.models import Item


class ItemCreateView(CreateView):
    model = Item
    template_name = "keys/create-item.html"
    fields = ['name']


class ItemListView(ListView):
    model = Item
    context_object_name = "items"
    template_name = "keys/list-item.html"
