from django.urls import path
from core.dashboard.views.home import homeviews as home
from core.dashboard.views.instrument import views as instrument
from core.dashboard.views.entity import views as entity
from core.dashboard.views.forms import formviews as forms

# define url patterns
urlpatterns = [
    path("", home.HomeView.as_view(), name="home"),
    path("instruments/", instrument.InstrumentView.as_view(), name="instruments"),
    path("api/instruments/", instrument.InstrumentApiView.as_view(), name="api-instruments"),
    path("entities/", entity.EntityView.as_view(), name="entities"),
    path("api/entities/", entity.EntityApiView.as_view(), name="api-entities"),
    path("forms/", forms.FormsViews.as_view(), name="forms-view"),
    path("forms/entity/", forms.EntityFormView.as_view(), name="entity-form"),
]
