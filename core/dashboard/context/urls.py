from django.urls import reverse
from pydantic import BaseModel


class UrlContext(BaseModel):
    instruments_url: str = reverse("instruments")
    home_url: str = reverse("home")
    entities_url: str = reverse("entities")
    forms_url: str = reverse("forms-view")
    entity_form_url: str = reverse("entity-form")
    entity_api_url: str = reverse("api-entities")


def get_url_context(_) -> UrlContext:
    return UrlContext().model_dump()
