from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def hello(request):
    result = {"message": "test", "data": "123", "label": "label"}

    return JsonResponse(result)
