from django.db import models
from django.apps import apps
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.ledger.models import Transaction, Entity  # noqa


class TransactionQueryManager(models.Manager):
    def prefetched_queryset(self) -> models.QuerySet["Transaction"]:
        Entity: "Entity" = apps.get_model("ledger", "Entity")  # noqa
        return self.get_queryset().prefetch_related(
            models.Prefetch(
                "entity", queryset=Entity.objects.select_related("instrument")
            ),
            "trx_category",
        )
