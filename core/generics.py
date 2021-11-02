from rest_framework import viewsets, mixins

class CreateUpdateDestroyListViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, mixins.ListModelMixin,
    viewsets.GenericViewSet
  ):

  pass
