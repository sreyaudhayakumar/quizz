from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only to ADMIN role users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "ADMIN"
