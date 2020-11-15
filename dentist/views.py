from rest_framework import mixins, viewsets

from dentist.models import Dentist
from dentist.serializers import DentistSerializer


class DentistViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Dentist.objects.all()
    serializer_class = DentistSerializer
    http_method_names = ['get']
