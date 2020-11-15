from rest_framework import mixins, viewsets, filters
from django_filters import rest_framework

from dentist.models import Dentist
from dentist.serializers import DentistSerializer


class DentistViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Dentist.objects.all()
    serializer_class = DentistSerializer
    http_method_names = ['get']
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = ('name', )
