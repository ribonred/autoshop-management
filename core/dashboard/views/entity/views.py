from django.views.generic import TemplateView
from core.ledger.models import Entity
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from core.dashboard.serializers.entity import EntitySerializer
from django.contrib.postgres.search import SearchVector
from django.db.models import TextField
from django.db.models.functions import Cast


class EntityView(TemplateView):
    template_name = "entity.html"


class EntityApiView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = "components/section/grid_entities.html"

    def get(self, request, *args, **kwargs):
        saerch = request.GET.get("search", None)
        attr = Cast("properties", TextField())
        entities = (
            Entity.objects.all()
            .only("code", "name", "properties")
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

    def post(self, request, *args, **kwargs):
        serializer = EntitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)
