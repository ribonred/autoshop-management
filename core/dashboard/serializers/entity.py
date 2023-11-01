from rest_framework import serializers

from core.ledger.models import Entity, Instrument


class EntitySerializer(serializers.ModelSerializer):
    instrument = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Instrument.objects.all().only("name"),
    )
    trx_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Entity
        fields = ("code", "name", "properties", "instrument", "id", "trx_count")
        extra_kwargs = {
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        return Entity.objects.create(**validated_data)
