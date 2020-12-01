from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_all', views.get_tasks, name='get_all'),
    path('add_task', views.post_task, name='add_task'),
    path('clear', views.delete_tasks, name='clear')
]
