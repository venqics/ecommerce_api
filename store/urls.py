from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('customers', views.CustomerViewSet)

urlpatterns = router.urls