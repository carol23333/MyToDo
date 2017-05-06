# coding: utf-8
from django.shortcuts import render
from rest_framework import viewsets

from tasks.permissions import TaskPermission
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (TaskPermission,)


def todolist(request):
    user_id = request.user.id
    return render(request, 'index.html', locals())
