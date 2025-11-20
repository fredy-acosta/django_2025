from rest_framework import viewsets
from .models import tax
from .serializers import TaxSerializer

class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
