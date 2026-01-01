from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntryViewSet, InsightsView

router = DefaultRouter()
router.register(r'entries', EntryViewSet, basename='entry')

urlpatterns = [
    path('', include(router.urls)),
    path('insights/', InsightsView.as_view(), name='insights'),
]
