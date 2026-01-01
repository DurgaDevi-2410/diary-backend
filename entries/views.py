from rest_framework import viewsets, permissions, views, response
from .models import Entry
from .serializers import EntrySerializer
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class InsightsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        now = timezone.now()
        last_30_days = now - timedelta(days=30)
        
        # Mood Breakdown
        mood_counts = Entry.objects.filter(user=user, created_at__gte=last_30_days).values('mood').annotate(count=Count('id'))
        
        # Total Entries
        total_entries = Entry.objects.filter(user=user).count()

        return response.Response({
            'mood_counts': mood_counts,
            'total_entries': total_entries
        })
