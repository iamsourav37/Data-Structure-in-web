from django.shortcuts import render, HttpResponse

# Create your views here.

ACTIVE = {"sorting_active": True}


def index(request):
    context = {
        "title": "Sorting",
        **ACTIVE
    }
    return render(request, "index.html", context)


def bubble_sort(request):
    context = {
        "title": "Bubble Sort",
        **ACTIVE,
    }
    
    return render(request, "bubble.html", context)