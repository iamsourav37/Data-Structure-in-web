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

    if request.method == "POST":
        #  extracting data
        raw_data = request.POST['values']
        values = raw_data.split(",")
        real_data = []
        print(values)
        try:
            for value in values:
                if len(value.strip()) > 0:
                    real_data.append(int(value))
        except Exception as e:
            context['msg'] = f"Something is wrong. Please enter comma separated value. Error message : {e}"
            return render(request, "bubble.html", context)

        print(real_data)
        context['unsorted_data'] = real_data.copy()

        # Bubble sort implementation
        for i in range(len(real_data)):
            is_sorted = True
            for j in range(len(real_data) - 1 - i):
                if real_data[j] > real_data[j + 1]:
                    real_data[j], real_data[j + 1] = real_data[j + 1], real_data[j]
                    is_sorted = False
            if is_sorted:
                break

        context["sorted_data"] = real_data

    return render(request, "bubble.html", context)
