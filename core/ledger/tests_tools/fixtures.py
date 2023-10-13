import factory
from factory import fuzzy
from pytest_factoryboy import register
from faker import Factory as FakerFactory
from core.ledger.models import Accounts, Instrument, TrxCategory, Transaction
from faker_vehicle import VehicleProvider

faker = FakerFactory.create()
faker.add_provider(VehicleProvider)


@register
class AccountsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Accounts

    account_name = factory.LazyAttribute(lambda _: faker.name())
    account_type = fuzzy.FuzzyChoice(Accounts.AccountType.choices)
    user = factory.SubFactory("core.authentication.tests_tools.fixtures.UserFactory")


@register
class InstrumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Instrument

    name = factory.LazyAttribute(lambda _: faker.vehicle_make())
    is_active = True


@register
class TrxCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TrxCategory

    name = fuzzy.FuzzyChoice(["SELL", "BUY", "REPAIR", "MAINTENANCE", "FUEL", "OTHER"])
    is_active = True


@register
class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    amount = fuzzy.FuzzyDecimal(0.01, 1000.00)
    description = factory.LazyAttribute(lambda _: faker.text())
    account = factory.SubFactory(AccountsFactory)
    trx_type = fuzzy.FuzzyChoice(Transaction.TransactionType.choices)
    instrument = factory.SubFactory(InstrumentFactory)

    @factory.post_generation
    def trx_category(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.trx_category.add(*extracted)
