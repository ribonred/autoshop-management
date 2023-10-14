import pytest
import structlog

logger = structlog.get_logger("test")


@pytest.mark.django_db
class TestLedgerModels:
    def test_ledger_accounts_factory(self, accounts_factory):
        account = accounts_factory()
        logger.debug(
            "test_ledger_accounts_factory",
            account_name=account.account_name,
            account_type=account.account_type,
            user=account.user.email,
        )
        assert account.account_name
        assert account.account_type
        assert account.user

    def test_instrument_factory(self, instrument_factory):
        instrument = instrument_factory()
        logger.debug(
            "test_instrument_factory",
            name=instrument.name,
            is_active=instrument.is_active,
        )
        assert instrument.name
        assert instrument.is_active

    def test_trx_category_factory(self, trx_category_factory):
        trx_category = trx_category_factory()
        logger.debug(
            "test_trx_category_factory",
            name=trx_category.name,
            is_active=trx_category.is_active,
        )
        assert trx_category.name
        assert trx_category.is_active

    def test_transaction_factory(self, transaction_factory):
        transaction = transaction_factory()
        logger.debug(
            "test_transaction_factory",
            amount=transaction.amount,
            description=transaction.description,
            account=transaction.account,
            trx_type=transaction.trx_type,
            entity=transaction.entity,
            trx_category=transaction.trx_category,
        )
        assert transaction.amount
        assert transaction.description
        assert transaction.account
        assert transaction.trx_type
        assert transaction.entity
        assert transaction.trx_category
