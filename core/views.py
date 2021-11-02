from rest_framework import viewsets, mixins, permissions
from rest_framework.permissions import SAFE_METHODS


class CreateUpdateDestroyListViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, mixins.ListModelMixin,
    viewsets.GenericViewSet
  ):

  pass



class IsAdminOrReadOnly(permissions.BasePermission):
  message = 'You are not authorized for this action.'

  def has_permission(self, request, view):
    IsAdmin = request.user.is_staff
    IsJustRead = request.method in SAFE_METHODS

    return IsAdmin or IsJustRead
