from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from tasks.serializer import TaskSerializer
from tasks.models import Task


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(["GET"])
def get_tasks(request):
    if request.method == 'GET':
        serializer = TaskSerializer(Task.objects.all(), many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

@api_view(["POST"])
def post_task(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@api_view(["DELETE"])
def delete_tasks(request):
    if request.method == 'DELETE':
        task = Task.objects.all().delete()
        return JsonResponse({"status": 200, "message": "Tasks deleted"}, status=200)
