from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, views, response


class CreateUpdateDestroyListViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, mixins.ListModelMixin,
    viewsets.GenericViewSet
  ):

  pass

class CreateUpdateDestroyViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, viewsets.GenericViewSet
  ):

  pass

class CreateDestroyListViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, 
    mixins.ListModelMixin, viewsets.GenericViewSet
  ):

  pass


class ToggleRecordGenericView(views.APIView):
  ''' Needed Fields
  model:Model
  lookup_field:str
  get_queryset_kwargs:function (kwargs for filter and create)
  '''

  def get(self, request, **kwargs):
    qs_kwargs = self.get_queryset_kwargs(request, **kwargs)
    self.model.objects.create(**qs_kwargs)

    return response.Response(status=201)

  def delete(self, request, **kwargs):
    qs_kwargs = self.get_queryset_kwargs(request, **kwargs)
    obj = get_object_or_404(self.model, **qs_kwargs)
    obj.delete()

    return response.Response(status=200)



