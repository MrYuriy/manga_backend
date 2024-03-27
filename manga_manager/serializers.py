from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.urls import reverse

from manga_manager.models import Chapter

class ChapterListSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = ("id", "chapter_name", "detail_url")

    def get_detail_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(reverse("manga_menager:chapter-detail", kwargs={"pk": obj.pk}))

class ChapterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ("id", "chapter_name", "urls_images_list")