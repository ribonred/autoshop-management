from django.urls import path
from core.dashboard.views.home import homeviews as home
from core.dashboard.views.instrument import views as instrument
from core.dashboard.views.entity import views as entity

# define url patterns
urlpatterns = [
    path("", home.HomeView.as_view(), name="home"),
    path("instruments/", instrument.InstrumentView.as_view(), name="instruments"),
    path("api/instruments/", instrument.InstrumentApiView.as_view(), name="api-instruments"),
    path("entities/", entity.EntityView.as_view(), name="entities"),
    path("api/entities/", entity.EntityApiView.as_view(), name="api-entities"),

]
