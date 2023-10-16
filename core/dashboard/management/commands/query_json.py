from django.core.management.base import BaseCommand
from core.dashboard.utils import entity_properties_keys


class Command(BaseCommand):
    help = "Generate dummy data for ledger models"

    def handle(self, *args, **options):
        keylist = entity_properties_keys()
        print(keylist)
