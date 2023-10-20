from rest_framework import serializers

from core.ledger.models import Instrument


class InstumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ("name",)

    def create(self, validated_data):
        return Instrument.objects.create(**validated_data)
