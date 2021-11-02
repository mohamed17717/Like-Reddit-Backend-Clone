from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrReadOnly(permissions.BasePermission):
  message = 'You are not authorized for this action.'

  def has_permission(self, request, view):
    IsAdmin = request.user.is_staff
    IsJustRead = request.method in SAFE_METHODS

    return IsAdmin or IsJustRead
