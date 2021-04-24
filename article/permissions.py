from django.http.request import HttpRequest
from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsSameSchool(BasePermission):
    def has_object_permission(self, request, view, obj):
        school_of_article = obj.school
        school_of_user = request.user.school
        return school_of_article == school_of_user


class IsWriterOrReadOnly(BasePermission):
    def has_object_permission(self, request: HttpRequest, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:  # if trying to delete or updateing the object
            user_of_article = obj.writer.username
            user = request.user.username
            return user_of_article == user