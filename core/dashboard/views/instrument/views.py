from django.views.generic import TemplateView
from core.ledger.models import Instrument
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count


class InstrumentView(TemplateView):
    template_name = "instrument.html"


class InstrumentApiView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

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
