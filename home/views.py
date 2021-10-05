from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title": "Home",
        "home_active": True,

    }
    return render(request, "home.html", context)
