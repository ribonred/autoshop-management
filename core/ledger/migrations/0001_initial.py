# Generated by Django 4.2.6 on 2023-10-14 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_lifecycle.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Accounts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "account_name",
                    models.CharField(max_length=255, verbose_name="Account Name"),
                ),
                (
                    "account_number",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Account Number",
                    ),
                ),
                (
                    "account_type",
                    models.CharField(
                        choices=[
                            ("ASSET", "Asset"),
                            ("LIABILITY", "Liability"),
                            ("EQUITY", "Equity"),
                            ("INCOME", "Income"),
                            ("EXPENSE", "Expense"),
                        ],
                        default="ASSET",
                        max_length=255,
                        verbose_name="Account Type",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, django_lifecycle.mixins.LifecycleModelMixin),
        ),
        migrations.CreateModel(
            name="Entity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "code",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Entity Code"
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Entity Name")),
                (
                    "properties",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        null=True,
                        verbose_name="Entity Properties",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, django_lifecycle.mixins.LifecycleModelMixin),
        ),
        migrations.CreateModel(
            name="Instrument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Instrument Name"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, django_lifecycle.mixins.LifecycleModelMixin),
        ),
        migrations.CreateModel(
            name="TrxCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Category Name"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, django_lifecycle.mixins.LifecycleModelMixin),
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Amount"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        default="no description", verbose_name="Description"
                    ),
                ),
                (
                    "trx_type",
                    models.CharField(
                        choices=[("DEBIT", "Debit"), ("CREDIT", "Credit")],
                        max_length=255,
                    ),
                ),
                (
                    "trx_date",
                    models.DateField(
                        default=django.utils.timezone.now,
                        verbose_name="Transaction Date",
                    ),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="ledger.accounts",
                        verbose_name="Account",
                    ),
                ),
                (
                    "entity",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trxs",
                        to="ledger.entity",
                        verbose_name="entity",
                    ),
                ),
                (
                    "trx_category",
                    models.ManyToManyField(
                        blank=True,
                        related_name="trx_categories",
                        to="ledger.trxcategory",
                        verbose_name="Transaction Category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, django_lifecycle.mixins.LifecycleModelMixin),
        ),
        migrations.AddField(
            model_name="entity",
            name="instrument",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="entities",
                to="ledger.instrument",
                verbose_name="Instrument",
            ),
        ),
    ]
