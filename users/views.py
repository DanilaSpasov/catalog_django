from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView


from users.forms import UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)

        send_mail(
            subject="Добро пожаловать!",
            message="Спасибо за регистрацию!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.object.email],
        )

        return response