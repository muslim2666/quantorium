from rest_framework.routers import DefaultRouter
from .views import VisitViewSet, PointViewSet

router = DefaultRouter()
router.register(r'visits', VisitViewSet)
router.register(r'points', PointViewSet)

urlpatterns = router.urls
