from django.views.generic import TemplateView
from core.ledger.models import Entity
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count


class EntityView(TemplateView):
    template_name = "entity.html"


class EntityApiView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        saerch = request.GET.get("search", None)
        entities = (
            Entity.objects.all()
            .only("code", "name", "properties")
            .annotate(trx_count=Count("trxs"))
            .prefetch_related("trxs")
        )
        if saerch:
            entities = entities.filter(name__icontains=saerch)
        return Response(
            {"entities": entities},
            template_name="components/section/grid_entities.html",
        )
