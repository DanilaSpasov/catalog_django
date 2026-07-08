from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
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
    form_class = ProductForm

class ProductCreateView(CreateView):
    model = Product
    template_name = "product_create.html"
    success_url = "/home/"
    form_class = ProductForm

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "product_update.html"
    pk_url_kwarg = "pk"
    form_class = ProductForm

    def get_success_url(self):
        return reverse("catalog:product_details", kwargs={"pk": self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_delete.html"
    pk_url_kwarg = "pk"
    success_url = "/home/"