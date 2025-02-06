from core.ledger.models import Entity, TrxCategory, Transaction
from rest_framework import serializers


class TransactionsSerializer(serializers.ModelSerializer):
    trx_category = serializers.SlugRelatedField(
        slug_field="name",
        queryset=TrxCategory.objects.all().only("name"),
    )
    trx_type = serializers.ChoiceField(
        choices=Transaction.TransactionType.choices,
    )
    trx_date = serializers.DateField(input_formats=["%d/%m/%Y", "%Y-%m-%d"])

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "account",
            "description",
            "entity",
            "trx_category",
            "trx_date",
            "trx_type",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "account": {"write_only": True, "required": False},
        }

    def validate(self, attrs):
        if not attrs.get("account"):
            attrs["account"] = self.context["user"].accounts.first()
        return attrs
