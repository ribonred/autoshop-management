import pytest
from core.dashboard.serializers.entity import EntitySerializer
from core.dashboard.serializers.instrument import InstumentSerializer


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
