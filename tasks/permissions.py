# -*- coding:utf-8 -*-
from rest_framework.permissions import BasePermission


class TaskPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
