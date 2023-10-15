from django.db import models
from helper.models import BaseTimeStampModel
from django.utils import timezone
from core.ledger.manager import TransactionQueryManager


class Accounts(BaseTimeStampModel):
    class AccountType(models.TextChoices):
        ASSET = "ASSET", "Asset"
        LIABILITY = "LIABILITY", "Liability"
        EQUITY = "EQUITY", "Equity"
        INCOME = "INCOME", "Income"
        EXPENSE = "EXPENSE", "Expense"

    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    account_name = models.CharField(max_length=255, verbose_name="Account Name")
    account_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Account Number"
    )
    account_type = models.CharField(
        max_length=255,
        verbose_name="Account Type",
        choices=AccountType.choices,
        default=AccountType.ASSET,
    )
    transactions: models.QuerySet["Transaction"]

    def __str__(self):
        return self.account_name


class Instrument(BaseTimeStampModel):
    name = models.CharField(max_length=255, verbose_name="Instrument Name", unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    trxs: models.QuerySet["Transaction"]

    def __str__(self):
        return self.name


class Entity(BaseTimeStampModel):
    instrument = models.ForeignKey(
        Instrument,
        on_delete=models.CASCADE,
        verbose_name="Instrument",
        null=True,
        blank=True,
        related_name="entities",
    )
    code = models.CharField(max_length=255, verbose_name="Entity Code", unique=True)
    name = models.CharField(max_length=255, verbose_name="Entity Name")
    properties = models.JSONField(
        verbose_name="Entity Properties", blank=True, null=True, default=dict
    )
    trxs: models.QuerySet["Transaction"]

    def __str__(self):
        return f"{self.name} - {self.code}"


class TrxCategory(BaseTimeStampModel):
    name = models.CharField(max_length=255, verbose_name="Category Name", unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    trx_categories: models.QuerySet["Transaction"]

    def __str__(self):
        return self.name


class Transaction(BaseTimeStampModel):
    class TransactionType(models.TextChoices):
        DEBIT = "DEBIT", "Debit"
        CREDIT = "CREDIT", "Credit"

    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Amount")
    description = models.TextField(verbose_name="Description", default="no description")
    account = models.ForeignKey(
        Accounts,
        on_delete=models.CASCADE,
        verbose_name="Account",
        related_name="transactions",
    )
    trx_category = models.ForeignKey(
        TrxCategory,
        verbose_name="Transaction Category",
        blank=True,
        null=True,
        related_name="trx_categories",
        on_delete=models.CASCADE,
    )
    trx_type = models.CharField(max_length=255, choices=TransactionType.choices)
    entity = models.ForeignKey(
        Entity,
        on_delete=models.CASCADE,
        verbose_name="entity",
        null=True,
        blank=True,
        related_name="trxs",
    )
    trx_date = models.DateField(verbose_name="Transaction Date", default=timezone.now)
    query_manager = TransactionQueryManager()

    def __str__(self):
        return self.description
