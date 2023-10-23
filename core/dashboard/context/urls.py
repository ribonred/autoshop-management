from django.urls import reverse
from pydantic import BaseModel


class UrlContext(BaseModel):
    entity_api_url: str = reverse("api-entities")
    entity_form_url: str = reverse("entity-form")
    entities_url: str = reverse("entities")
    forms_url: str = reverse("forms-view")
    home_url: str = reverse("home")
    instrument_api_url: str = reverse("api-instruments")
    instrument_form_url: str = reverse("instrument-form")
    instruments_url: str = reverse("instruments")
    transactions_url: str = reverse("transactions")
    transaction_form_url: str = reverse("transaction-form")
    transaction_api_url: str = reverse("api-transactions")


def get_url_context(_) -> UrlContext:
    return UrlContext().model_dump()
