from rest_framework import routers
from .api import populate_api

router = routers.DefaultRouter()
populate_api(router)
urlpatterns = router.urls

