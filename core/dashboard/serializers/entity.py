from rest_framework import serializers

from core.ledger.models import Entity, Instrument


class EntitySerializer(serializers.ModelSerializer):
    instrument = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Instrument.objects.all().only("name"),
    )

    class Meta:
        model = Entity
        fields = ("code", "name", "properties", "instrument")

    def create(self, validated_data):
        return Entity.objects.create(**validated_data)
