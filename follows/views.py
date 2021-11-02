from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import views, permissions
from rest_framework.response import Response

from follows.models import UserFollow, ThreadFollow
from accounts.serializers import UserBasicPublicSerializer
from core.generics import ToggleRecordGenericView
from threads.models import Thread


User = get_user_model()


class UserFollow_ToggleFollow_ApiView(ToggleRecordGenericView):
  model = UserFollow
  lookup_field = 'username'
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset_kwargs(self, request, **kwargs):
    username = kwargs.get(self.lookup_field, '')

    target = get_object_or_404(User, username=username)
    follower = request.user

    return {'target': target, 'follower': follower}


class UserFollow_CheckFollow_ApiView(views.APIView):
  model = UserFollow
  lookup_field = 'username'
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset_kwargs(self, request, **kwargs):
    username = kwargs.get(self.lookup_field, '')

    target = get_object_or_404(User, username=username)
    follower = request.user

    return {'target': target, 'follower': follower}

  def get(self, request, **kwargs):
    qs_kwargs = self.get_queryset_kwargs(request, **kwargs)
    get_object_or_404(self.model, **qs_kwargs)

    return Response(200)


class UserFollow_ListFollows_ApiView(views.APIView):
  ''' People he has follows '''
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request, **kwargs):
    qs = User.objects.filter(user_followers__follower=request.user)
    serialized = UserBasicPublicSerializer(qs, many=True)

    return Response(serialized.data)


class UserFollow_ListFollowers_ApiView(views.APIView):
  ''' People follows him '''
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request, **kwargs):
    qs = User.objects.filter(user_targets__target=request.user)
    serialized = UserBasicPublicSerializer(qs, many=True)

    return Response(serialized.data)


class ThreadFollow_ToggleFollow_ApiView(ToggleRecordGenericView):
  model = ThreadFollow
  lookup_field = 'thread_id'
  permission_classes = [permissions.IsAuthenticated]
  
  def get_queryset_kwargs(self, request, **kwargs):
    thread_id = kwargs.get(self.lookup_field, '')

    target = get_object_or_404(Thread, id=thread_id)
    follower = request.user

    return {'target': target, 'follower': follower}



