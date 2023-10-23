from typing import Any
from django.views.generic import TemplateView
from core.ledger.models import TrxCategory, Transaction


class FormsViews(TemplateView):
    template_name = "forms.html"


class EntityFormView(TemplateView):
    template_name = "components/forms/entity_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instrument = self.request.GET.get("instrument", None)
        context["instrument_param"] = instrument or ""
        return context


class TransactionFormView(TemplateView):
    template_name = "components/forms/transaction_form.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = [
            {"id": category.id, "name": category.name}
            for category in TrxCategory.objects.all()
        ]
        context["directions"] = [
            {"id": direction[0], "name": direction[1]}
            for direction in Transaction.TransactionType.choices
        ]
        return context


class InstrumentFormView(TemplateView):
    template_name = "components/forms/instrument_form.html"
