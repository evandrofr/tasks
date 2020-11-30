from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Task
from .serializer import Serializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(["get"])
def get_task(request: HttpRequest):
    all_tasks = Task.objects.all()
    serializer = Serializer(all_tasks, many =True)
    return JsonResponse(serializer.data, safe =False)