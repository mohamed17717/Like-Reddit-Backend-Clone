from rest_framework import permissions
from rest_framework.exceptions import APIException
from rest_framework.permissions import SAFE_METHODS
from rest_framework.status import HTTP_403_FORBIDDEN


class IsAdminOrReadOnly(permissions.BasePermission):
  message = 'You are not authorized for this action.'

  def has_permission(self, request, view):
    IsAdmin = request.user.is_staff
    IsJustRead = request.method in SAFE_METHODS

    return IsAdmin or IsJustRead


class IsUserNotBanned(permissions.BasePermission):
  message = 'You can\'t do this action because you are banned right now.'

  def has_permission(self, request, view):
    user = request.user
    return not (user.is_authenticated and user.is_banned)


class IsUserHasAccessToThisContent:
  message = 'You can\'t access private content.'
  code = HTTP_403_FORBIDDEN

  def __init__(self, request, instance, raise_exception=True) -> None:
    self.request = request
    self.instance = instance
    self.raise_exception = raise_exception

    return self.check()

  def is_instance_private(self) -> bool:
    return self.instance.is_private
  
  def is_user_has_access(self) -> bool:
    user = self.request.user
    return user.is_authenticated and (user.is_premium or user.is_stuff)
  
  def check(self):
    state = True

    if self.is_instance_private() and not self.is_user_has_access():
      state = False

      if self.raise_exception:
        raise APIException(detail=self.message, code=self.code)

    return state

