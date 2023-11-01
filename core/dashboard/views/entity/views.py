from typing import Any
from django.views.generic import TemplateView
from core.ledger.models import Entity
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from django.db.models import Count
from core.dashboard.serializers.entity import EntitySerializer
from django.contrib.postgres.search import SearchVector
from django.db.models import TextField
from django.db.models.functions import Cast
from rest_framework import mixins, viewsets


class EntityView(TemplateView):
    template_name = "entity.html"


class EntityDetailView(TemplateView):
    template_name = "pages/entity_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(kwargs)
        return context


class EntityApiView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = "components/section/grid_entities.html"
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    def list(self, request, *args, **kwargs):
        saerch = request.GET.get("search", None)
        attr = Cast("properties", TextField())
        entities = (
            self.queryset.only("code", "name", "properties")
            .annotate(
                trx_count=Count("trxs"), search=SearchVector("name", "code", attr)
            )
            .prefetch_related("trxs")
        )
        if saerch:
            entities = entities.filter(search__icontains=saerch)
        serializer = EntitySerializer(entities, many=True)
        return Response(
            {"entities": serializer.data},
        )
