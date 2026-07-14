from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.forms import ProductForm, ModeratorProductForm
from catalog.models import Product, Category
from catalog.services import get_products_by_category


class HomeView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "product_list"


class ContactsView(ListView):
    model = Product
    template_name = "contacts.html"
    context_object_name = "product_list"

class ProductsByCategoryView(ListView):
    model = Product
    template_name = "products_by_category.html"
    context_object_name = "products_by_category"

    def get_queryset(self):
        return get_products_by_category(self.kwargs["category_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(pk=self.kwargs["category_id"])
        context["category_title"] = category.title
        context["category_description"] = category.description
        return context


@method_decorator(cache_page(60), name='dispatch')
class ProductDetailsView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"
    form_class = ProductForm


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "product_create.html"
    success_url = "/home/"
    form_class = ProductForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "product_update.html"
    pk_url_kwarg = "pk"

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner == request.user:
            return super().dispatch(request, *args, **kwargs)
        if request.user.has_perm("catalog.can_unpublish_product"):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

    def get_form_class(self):
        if self.request.user.has_perm("catalog.can_unpublish_product"):
            return ModeratorProductForm
        return ProductForm

    def get_success_url(self):
        return reverse("catalog:product_details", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_delete.html"
    pk_url_kwarg = "pk"
    success_url = "/home/"

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.has_perm(
            "catalog.delete_product"
        ):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
