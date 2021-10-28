from django.shortcuts import render, HttpResponse
import numpy as np
from numpy.lib.type_check import real

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
        real_data = np.array([])
        try:
            real_data = np.array(extract_real_data(values))
        except Exception as e:
            context['msg'] = f"Something is wrong. Please enter comma separated value. **(Error message : {e})"
            return render(request, "bubble.html", context)

        context['unsorted_data'] = np.copy(real_data)

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

        real_data = np.array([])

        try:
            real_data = np.array(extract_real_data(values))
            print(real_data)
        except Exception as e:
            context['msg'] = f"Something is wrong. Please enter comma separated value. **(Error message : {e})"
            return render(request, "insertion_sort.html", context)
        context['unsorted_data'] = list(np.copy(real_data))

        # insertion sort implementation
        for i in range(1, len(real_data)):
            j = i - 1
            key = real_data[i]
            while j >= 0 and real_data[j] > key:
                real_data[j+1] = real_data[j]
                j -= 1
            real_data[j+1] = key
        context['sorted_data'] = list(real_data)

    return render(request, "insertion_sort.html", context)


def selection_sort(request):
    context = {
        "title": "Selection Sorting",
        **ACTIVE
    }

    if request.method == 'POST':
        raw_data = request.POST['values']
        values = raw_data.split(",")
        real_data = np.array([])
        try:
            real_data = np.array(extract_real_data(values))
        except Exception as e:
            context['msg'] = f"Something is wrong. Please enter comma separated value. **(Error message : {e})"
            return render(request, "selection_sort.html", context)

        context['unsorted_data'] = list(np.copy(real_data))
        print(real_data)
        #  23 3 6 8 0
        # selection sort implementation
        for i in range(len(real_data)):
            index_of_min_value = i
            for j in range(i+1, len(real_data)):
                if real_data[index_of_min_value] > real_data[j]:
                    index_of_min_value = j
            real_data[i], real_data[index_of_min_value] = real_data[index_of_min_value], real_data[i]
        context['sorted_data'] = list(real_data)

    return render(request, "selection_sort.html", context)


