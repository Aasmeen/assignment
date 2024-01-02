from rest_framework import permissions

class CanCreateorDeleteItem(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_admin

class CanUpdateItem(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_admin or request.user.is_content_editor)
