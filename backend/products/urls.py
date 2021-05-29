from django.urls import path, include

from .views import LatestProductsList

urlpatterns = [
    path('latest/', LatestProductsList.as_view())
]
