import pytest
from core.dashboard.serializers.entity import EntitySerializer
from core.dashboard.serializers.instrument import InstumentSerializer
from django.urls import reverse
import json

from core.dashboard.serializers.transactions import TransactionsSerializer


@pytest.mark.django_db
class TestDashboard:
    def test_entity_serializer(self, instrument_factory):
        instrument = instrument_factory()
        data = {
            "code": "code",
            "name": "name",
            "properties": {"key": "value"},
            "instrument": instrument.name,
        }
        serializer = EntitySerializer(data=data)
        is_valid = serializer.is_valid()
        assert is_valid
        serializer.save()

    def test_instrument_serializer(self):
        data = {"name": "name"}
        serializer = InstumentSerializer(data=data)
        is_valid = serializer.is_valid(raise_exception=True)
        assert is_valid
        serializer.save()
        assert serializer.data == data

    def test_transaction_serializer(
        self, trx_category_factory, entity_factory, accounts_factory
    ):
        trx_category = trx_category_factory()
        entity = entity_factory()
        account = accounts_factory()
        data = {
            "amount": 1000,
            "account": account.pk,
            "description": "description",
            "entity": entity.pk,
            "trx_category": trx_category.name,
            "trx_date": "01/01/2021",
            "trx_type": "DEBIT",
        }
        serializer = TransactionsSerializer(data=data)
        is_valid = serializer.is_valid(raise_exception=True)
        assert is_valid
        serializer.save()
        data["trx_date"] = "2021-01-01"
        serializer = TransactionsSerializer(data=data)
        is_valid = serializer.is_valid(raise_exception=True)
        assert is_valid
        serializer.save()

    def test_api_entites(self, client, instrument_factory):
        url = reverse("api-entities")
        instrument = instrument_factory()
        response = client.post(
            url,
            json.dumps(
                {
                    "instrument": instrument.name,
                    "name": "name",
                    "code": "code",
                    "properties": {"dadang": "xxx", "bajul": "xxxx"},
                }
            ),
            content_type="application/json",
        )
        assert response.status_code == 201

    def test_api_instruments(self, client):
        url = reverse("api-instruments")
        response = client.post(
            url,
            json.dumps(
                {
                    "name": "name",
                }
            ),
            content_type="application/json",
        )
        assert response.status_code == 201

    def test_api_transaction(
        self, client, trx_category_factory, entity_factory, accounts_factory
    ):
        url = reverse("api-transactions")
        trx_category = trx_category_factory()
        entity = entity_factory()
        _ = accounts_factory(user__username="admin", user__password="admin")
        client.login(username="admin", password="admin")
        response = client.post(
            url,
            json.dumps(
                {
                    "amount": 1000,
                    "description": "description",
                    "entity": entity.pk,
                    "trx_category": trx_category.name,
                    "trx_date": "01/01/2021",
                    "trx_type": "DEBIT",
                }
            ),
            content_type="application/json",
        )
        assert response.status_code == 201
