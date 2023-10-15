from django.urls import path
from core.dashboard.views.home import homeviews as home
from core.dashboard.views.instrument import views as instrument

# define url patterns
urlpatterns = [
    path("", home.HomeView.as_view(), name="home"),
    path("instruments/", instrument.InstrumentView.as_view(), name="instruments"),
]
