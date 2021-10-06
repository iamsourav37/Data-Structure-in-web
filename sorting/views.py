from django.shortcuts import render, HttpResponse

# Create your views here.

ACTIVE = {"sorting_active": True}


def extract_real_data(values):
    real_data = []
    for value in values:
        if len(value.strip()) > 0:
            real_data.append(int(value))
    return real_data


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
        try:
            real_data = extract_real_data(values)
        except Exception as e:
            context['msg'] = f"Something is wrong. Please enter comma separated value. **(Error message : {e})"
            return render(request, "bubble.html", context)

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


def insertion_sort(request):
    context = {
        "title": "Insertion Sort",
        **ACTIVE
    }

    if request.method == 'POST':
        raw_data = request.POST['values']
        print(raw_data)
        values = raw_data.split(",")
        print(values)

        real_data = []

        try:
            real_data = extract_real_data(values)
            print(real_data)
        except Exception as e:
            context['msg'] = f"Something is wrong. Please enter comma separated value. **(Error message : {e})"
            return render(request, "insertion_sort.html", context)
        context['unsorted_data'] = real_data.copy()

        # insertion sort implementation
        for i in range(1, len(real_data)):
            j = i - 1
            key = real_data[i]
            while j >= 0 and real_data[j] > key:
                real_data[j+1] = real_data[j]
                j -= 1
            real_data[j+1] = key
        context['sorted_data'] = real_data

    return render(request, "insertion_sort.html", context)
