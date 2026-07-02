from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


class HomeView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "product_list"


class ContactsView(ListView):
    model = Product
    template_name = "contacts.html"
    context_object_name = "product_list"


class ProductDetailsView(DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"
