from django.urls import path
from .views import ChapterListView

urlpatterns = [
    path("chapters/", ChapterListView.as_view(), name="chapter-list"),
]