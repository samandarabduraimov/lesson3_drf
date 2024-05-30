from rest_framework.routers import DefaultRouter
from .views import UserViewsets


router = DefaultRouter()
router.register('users', UserViewsets, basename='users')
urlpatterns = router.urls