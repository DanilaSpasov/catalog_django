import os

from django.core.management import BaseCommand

from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        email = os.getenv("SUPERUSER_EMAIL")
        password = os.getenv("SUPERUSER_PASSWORD")

        if not email or not password:
            self.stdout.write(
                self.style.ERROR("Не заданы данные суперпользователя в .env")
            )
            return

        user = User.objects.create(
            email=email,
            is_staff=True,
            is_superuser=True,
        )

        user.set_password(password)
        user.save()

        self.stdout.write(self.style.SUCCESS("Суперпользователь создан"))
