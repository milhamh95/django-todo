from django.urls import path
from .views import IndexView, DetailView

urlpatterns = [
    path("", IndexView.as_view(), name="index_view"),
    path("todos/<str:id>/", DetailView.as_view(), name="detail_view")
]