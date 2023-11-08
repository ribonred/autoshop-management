from core.authentication.models import User
from core.ledger.models import Transaction
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from rest_framework.views import APIView
from core.dashboard.serializers.transactions import TransactionsSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin


class TransactionsApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TransactionsSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class TransactionView(LoginRequiredMixin, TemplateView):
    template_name = "transactions.html"

    def get_context_data(self, **kwargs):
        page_num: int = self.request.GET.get("page", 1)
        user: User = self.request.user
        context = super().get_context_data(**kwargs)
        transactions = Transaction.query_manager.transaction_user(user.id).order_by(
            "-created"
        )
        paginator = Paginator(transactions, 10)
        trx_obj = paginator.get_page(page_num)
        context["transactions"] = trx_obj
        context["data_count"] = paginator.count
        return context
