from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TestViewSet, TestResultViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'tests', TestViewSet)
router.register(r'results', TestResultViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]
