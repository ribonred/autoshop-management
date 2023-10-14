from django.views.generic import TemplateView
from core.ledger.models import Transaction, Entity
from django.db.models import Prefetch
from django.utils import timezone


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = Transaction.objects.prefetch_related(
            Prefetch("entity", queryset=Entity.objects.select_related("instrument")),
            "trx_category",
        ).filter(account__user=self.request.user)
        today_trx = transactions.filter(trx_date=timezone.now().date())
        yesterday_trx = transactions.filter(
            trx_date=timezone.now().date() - timezone.timedelta(days=1)
        )
        context["today_trx"] = today_trx
        context["yesterday_trx"] = yesterday_trx
        return context
