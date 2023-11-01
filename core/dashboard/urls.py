from django.urls import path
from core.dashboard.views.home import homeviews as home
from core.dashboard.views.instrument import views as instrument
from core.dashboard.views.transactions import views as transactions
from core.dashboard.views.entity import views as entity
from core.dashboard.views.forms import formviews as forms

# define url patterns
urlpatterns = [
    path("", home.HomeView.as_view(), name="home"),
    path("instruments/", instrument.InstrumentView.as_view(), name="instruments"),
    path("transactions/", transactions.TransactionView.as_view(), name="transactions"),
    path(
        "api/transactions/",
        transactions.TransactionsApiView.as_view(),
        name="api-transactions",
    ),
    path(
        "api/instruments/",
        instrument.InstrumentApiView.as_view(),
        name="api-instruments",
    ),
    path("entities/", entity.EntityView.as_view(), name="entities"),
    path("entities/<int:pk>/", entity.EntityDetailView.as_view(), name="entities-detail"),
    path(
        "api/entities/",
        entity.EntityApiView.as_view({"get": "list", "post": "create"}),
        name="api-entities",
    ),
    path(
        "api/entities/<int:pk>/",
        entity.EntityApiView.as_view({"get": "retrieve"}),
        name="api-entity-detail",
    ),
    path("forms/", forms.FormsViews.as_view(), name="forms-view"),
    path("forms/entity/", forms.EntityFormView.as_view(), name="entity-form"),
    path(
        "forms/instrument/", forms.InstrumentFormView.as_view(), name="instrument-form"
    ),
    path(
        "forms/transaction/",
        forms.TransactionFormView.as_view(),
        name="transaction-form",
    ),
]
