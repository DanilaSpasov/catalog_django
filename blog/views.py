from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)

from blog.models import Blog


class BlogView(ListView):
    model = Blog
    template_name = "blog.html"
    context_object_name = "blog_list"

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class BlogDetailsView(DetailView):
    model = Blog
    template_name = "blog_details.html"
    context_object_name = "blog"
    pk_url_kwarg = "pk"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blog_create.html"
    fields = ["title", "content", "preview_image", "is_published"]
    success_url = "/blog/"


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "blog_update.html"
    fields = ["title", "content", "preview_image", "is_published"]
    pk_url_kwarg = "pk"

    def get_success_url(self):
        return reverse("blog:blog_details", kwargs={"pk": self.object.pk})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog_delete.html"
    success_url = "/blog/"
    pk_url_kwarg = "pk"
