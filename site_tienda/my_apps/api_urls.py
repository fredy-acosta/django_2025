from rest_framework.routers import DefaultRouter
from my_apps.category.views import CategoryViewSet
from my_apps.product.views import ProductViewSet
from my_apps.tax.views import TaxViewSet
from my_apps.branch.views import BranchViewSet
from my_apps.inventory.views import InventoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'taxes', TaxViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'inventories', InventoryViewSet)

urlpatterns = router.urls
