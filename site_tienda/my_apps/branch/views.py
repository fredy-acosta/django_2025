from rest_framework import viewsets
from .models import branch
from .serializers import BranchSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
