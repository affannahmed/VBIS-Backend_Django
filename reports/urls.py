from rest_framework.routers import DefaultRouter
from .views import (ArtilleryReportViewSet, ContactReportViewSet,
                    AFVStateReportViewSet, AmmoStateReportViewSet,
                    FuelStateReportViewSet)

router = DefaultRouter()
router.register(r'artillery-reports', ArtilleryReportViewSet)
router.register(r'contact-reports', ContactReportViewSet)
router.register(r'rafv-reports', AFVStateReportViewSet)
router.register(r'ammo-reports', AmmoStateReportViewSet)
router.register(r'fuel-reports', FuelStateReportViewSet)

urlpatterns = router.urls
