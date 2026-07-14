from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create moderator group"

    def handle(self, *args, **options):
        moderator_group, created = Group.objects.get_or_create(
            name="Модератор продуктов"
        )
        unpublish_permission = Permission.objects.get(
            codename="can_unpublish_product",
            content_type__app_label="catalog",
        )
        delete_permission = Permission.objects.get(
            codename="delete_product",
            content_type__app_label="catalog",
        )
        moderator_group.permissions.add(unpublish_permission, delete_permission)
