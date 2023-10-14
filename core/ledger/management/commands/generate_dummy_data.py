from django.core.management.base import BaseCommand
from core.ledger.tests_tools.fixtures import AccountsFactory, InstrumentFactory, EntityFactory, TrxCategoryFactory, TransactionFactory

class Command(BaseCommand):
    help = 'Generate dummy data for ledger models'

    def handle(self, *args, **options):
        # Create dummy data
        AccountsFactory.create_batch(10)
        InstrumentFactory.create_batch(10)
        EntityFactory.create_batch(10)
        TrxCategoryFactory.create_batch(10)
        TransactionFactory.create_batch(50)

        self.stdout.write(self.style.SUCCESS('Successfully generated dummy data'))
