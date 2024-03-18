from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from manga_manager.models import Chapter

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ("chapter_name", "urls_images_list")
