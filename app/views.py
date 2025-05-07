from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random


def lotto(request):
    numbers = sorted(random.sample(range(1, 50), 6))
    spec_number = random.randint(1, 49)

    numbers = " ".join([str(i) for i in numbers])
    # numbers = " ".join(map(str, numbers))

    result = {"number": numbers, "spec_number": spec_number}

    return render(request, "lotto.html", result)


# Create your views here.
def hello(request):
    result = {"message": "test", "data": "123", "label": "label"}
    return JsonResponse(result)
