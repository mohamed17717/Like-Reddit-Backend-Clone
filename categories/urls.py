from rest_framework import routers
from .views import Category_ApiView, SubCategory_ApiView

app_name = 'categories'

router = routers.SimpleRouter()

router.register(r'category', Category_ApiView)
router.register(r'sub-category', SubCategory_ApiView)

urlpatterns = router.urls
