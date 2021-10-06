from django.urls import path

from .views import index, bubble_sort, insertion_sort, selection_sort

urlpatterns = [
    path("", index, name="sorting-home"),
    path("bubble-sort/", bubble_sort, name="bubble-sort"),
    path("insertion-sort/", insertion_sort, name="insertion-sort"),
    path("selection-sort/", selection_sort, name="selection-sort"),

]