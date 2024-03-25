from django.urls import path, include
from .views import ChapterViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register("chapters", ChapterViewSet)
urlpatterns = [
    path("", include(router.urls))
]
app_name = "manga_menager"