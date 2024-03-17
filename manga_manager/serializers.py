from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from manga_manager.models import Chapter

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ("chapter_name", "urls_images_list")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            "id": representation["id"],
            "chapter_name": representation["chapter_name"],
            "urls_images_list": representation["urls_images_list"]
        }