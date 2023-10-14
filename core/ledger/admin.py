from django.contrib import admin
from .models import Accounts, Instrument, TrxCategory, Transaction


@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display = (
        "account_name",
        "account_type",
    )
    list_filter = ("account_type", "account_type")
    search_fields = ("account_name",)


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(TrxCategory)
class TrxCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("amount", "description", "account", "trx_type", "entity")
    list_filter = ("trx_type", "account", "entity")
    search_fields = ("description",)
