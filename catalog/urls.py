from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductDetailsView, HomeView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailsView.as_view(), name="product_details"),
]
