from django.urls import reverse
from pydantic import BaseModel


class UrlContext(BaseModel):
    instruments_url: str = reverse("instruments")
    home_url: str = reverse("home")
    entities_url: str = reverse("entities")


def get_url_context(_) -> UrlContext:
    return UrlContext().model_dump()
