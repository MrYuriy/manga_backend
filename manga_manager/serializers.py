from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from manga_manager.models import Chapter

class ChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ("id", "chapter_name")

class ChapterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ("id", "chapter_name", "urls_images_list")