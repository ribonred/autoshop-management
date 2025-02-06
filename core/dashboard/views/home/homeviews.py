from django.views.generic import TemplateView
from core.ledger.models import Transaction
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = Transaction.query_manager.prefetched_queryset().filter(
            account__user=self.request.user
        )
        today_trx = transactions.filter(trx_date=timezone.now().date())
        yesterday_trx = transactions.filter(
            trx_date=timezone.now().date() - timezone.timedelta(days=1)
        )
        context["today_trx"] = today_trx
        context["yesterday_trx"] = yesterday_trx
        return context
