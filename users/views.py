from django.views.generic import CreateView
from users.forms import UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = "/users/login/"
    template_name = "register.html"

