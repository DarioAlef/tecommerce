from rest_framework import routers
from teste import views

router = routers.DefaultRouter()
router.register('clients', views.ClientViewSet)
router.register('products', views.ProductViewSet)
router.register('employees', views.EmployeeViewSet)
router.register('sales', views.SaleViewSet)

urlpatterns = router.urls