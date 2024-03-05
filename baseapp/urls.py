from django.urls import path, include
from baseapp import views

urlpatterns = [
    path("", views.home, name="homepage"),
]
