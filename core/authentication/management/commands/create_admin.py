from django.core.management.base import BaseCommand
from core.authentication.models import User

class Command(BaseCommand):
    help = "Generate superuser"

    def handle(self, *args, **options):
        superuser = User.objects.get_superuser()
        if not superuser.exists():
            _ = User.objects.create_superuser(
                email="admin@admin.com",
                username="admin",
                password="admin",
            )
