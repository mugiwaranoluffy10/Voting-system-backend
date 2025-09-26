from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Category, Nomination, JuryReview
from .serializers import CategorySerializer, NominationSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class NominationViewSet(viewsets.ModelViewSet):
    queryset = Nomination.objects.all()
    serializer_class = NominationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def approve(self, request, pk=None):
        nomination = self.get_object()
        nomination.status = 'Approved'
        nomination.save()
        JuryReview.objects.create(
            nomination=nomination,
            reviewer=request.user,
            status='Approved'
        )
        return Response({"status": "approved"})

