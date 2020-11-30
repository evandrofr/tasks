from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.serializer import TaskSerializer
from tasks.models import Task


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get_tasks(request):
    # if request.method == 'GET':
    #     serializer = TaskSerializer(Task.objects.all(), many=True)
    #     return JsonResponse(serializer.data, safe=False)
    return {'status': 200}