import pytest
from core.dashboard.serializers.entity import EntitySerializer
from core.dashboard.serializers.instrument import InstumentSerializer
from django.urls import reverse
import json


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
        assert serializer.data == data

    def test_instrument_serializer(self):
        data = {"name": "name"}
        serializer = InstumentSerializer(data=data)
        is_valid = serializer.is_valid()
        assert is_valid
        serializer.save()
        assert serializer.data == data

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
