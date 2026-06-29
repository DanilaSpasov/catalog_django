from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {"product_list": product_list}
    return render(request, "home.html", context)


def contacts(request):
    return render(request, "contacts.html")


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_details.html", {"product": product})
