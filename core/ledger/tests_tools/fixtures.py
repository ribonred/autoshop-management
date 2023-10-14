import factory
from factory import fuzzy
from pytest_factoryboy import register
from faker import Factory as FakerFactory
from core.ledger import models as ledger_models
from faker_vehicle import VehicleProvider

faker = FakerFactory.create()
faker.add_provider(VehicleProvider)


@register
class AccountsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ledger_models.Accounts

    account_name = factory.LazyAttribute(lambda _: faker.name())
    account_type = fuzzy.FuzzyChoice(ledger_models.Accounts.AccountType)
    user = factory.SubFactory("core.authentication.tests_tools.fixtures.UserFactory")


@register
class InstrumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ledger_models.Instrument

    name = factory.LazyAttribute(lambda _: faker.vehicle_make_model())
    is_active = True


@register
class EntityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ledger_models.Entity

    name = factory.LazyAttribute(lambda _: faker.machine_category())
    code = factory.LazyAttribute(lambda _: faker.lexify(text="?????"))
    instrument = factory.SubFactory(InstrumentFactory)


@register
class TrxCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ledger_models.TrxCategory

    name = factory.Iterator(["SELL", "BUY", "REPAIR", "MAINTENANCE", "FUEL", "OTHER"])
    is_active = True


@register
class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ledger_models.Transaction

    amount = fuzzy.FuzzyDecimal(2_000_000, 50_000_000, 2)
    description = factory.LazyAttribute(lambda _: faker.text())
    account = factory.SubFactory(AccountsFactory)
    trx_type = fuzzy.FuzzyChoice(ledger_models.Transaction.TransactionType)
    trx_category = factory.SubFactory(TrxCategoryFactory)
    entity = factory.SubFactory(EntityFactory)
    trx_date = factory.LazyAttribute(
        lambda _: faker.date_between(start_date="-2d", end_date="today")
    )
