from django.urls import path

from .views import index, bubble_sort

urlpatterns = [
    path("", index, name="sorting-home"),
    path("bubble/", bubble_sort, name="bubble-sort")
]