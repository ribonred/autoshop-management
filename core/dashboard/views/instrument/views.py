from django.views.generic import TemplateView
from core.ledger.models import Instrument
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as api_status
from django.db.models import Count
from core.dashboard.serializers.instrument import InstumentSerializer
from django.contrib.auth.mixins import LoginRequiredMixin


class InstrumentView(LoginRequiredMixin, TemplateView):
    template_name = "instrument.html"


class InstrumentApiView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        saerch = request.GET.get("search", None)
        instruments = (
            Instrument.objects.all()
            .only("name")
            .annotate(entity_count=Count("entities"))
            .prefetch_related("entities")
        )
        if saerch:
            instruments = instruments.filter(name__icontains=saerch)
        return Response(
            {"instruments": instruments},
            template_name="components/section/grid_instrument.html",
        )

    def post(self, request, *args, **kwargs):
        serializer = InstumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"instruments": serializer.data}, status=api_status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=400)
