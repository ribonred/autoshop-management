from django.core.management.base import BaseCommand
from core.ledger.tests_tools.fixtures import (
    AccountsFactory,
    InstrumentFactory,
    EntityFactory,
    TrxCategoryFactory,
    TransactionFactory,
)
from core.authentication.models import User


class Command(BaseCommand):
    help = "Generate dummy data for ledger models"

    def handle(self, *args, **options):
        # Create dummy data
        user = User.objects.get(username="admin")
        account = AccountsFactory.create(user=user)
        instrument = InstrumentFactory.create()
        entity = EntityFactory.create(instrument=instrument)
        TransactionFactory.create_batch(50, account=account, entity=entity)

        self.stdout.write(self.style.SUCCESS("Successfully generated dummy data"))
