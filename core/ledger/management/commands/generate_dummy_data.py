from django.core.management.base import BaseCommand
from core.ledger.tests_tools.fixtures import (
    AccountsFactory,
    InstrumentFactory,
    EntityFactory,
    TrxCategoryFactory,
    TransactionFactory,
)
from core.authentication.models import User
from django.db import transaction
import factory


class Command(BaseCommand):
    help = "Generate dummy data for ledger models"

    def handle(self, *args, **options):
        # Create dummy data
        user = User.objects.get(username="admin")
        with transaction.atomic():
            account = AccountsFactory.create(user=user)
            instrument = InstrumentFactory.create()
            entity = EntityFactory.create(instrument=instrument)
            trx_category = TrxCategoryFactory.create_batch(
                6,
                name=factory.Iterator(
                    ["SELL", "BUY", "REPAIR", "MAINTENANCE", "FUEL", "OTHER"]
                ),
            )
            TransactionFactory.create_batch(
                50,
                account=account,
                entity=entity,
                trx_category=factory.Iterator(trx_category),
            )

        self.stdout.write(self.style.SUCCESS("Successfully generated dummy data"))
