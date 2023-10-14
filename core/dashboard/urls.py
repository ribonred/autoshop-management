from django.urls import path
from .views.homeviews import HomeView

# define url patterns
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
