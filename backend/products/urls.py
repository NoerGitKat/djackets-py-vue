from django.urls import path, include

from .views import LatestProductsList, ProductDetail

urlpatterns = [
    path('latest/', LatestProductsList.as_view()),
    path('latest/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view())
]
