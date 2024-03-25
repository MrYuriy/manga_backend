
from rest_framework import mixins, viewsets
from .models import Chapter
from .serializers import ChapterListSerializer, ChapterDetailSerializer
from rest_framework.response import Response



class ChapterViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, 
    mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Chapter.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        sorted_queryset = sorted(
            queryset, 
            key=lambda chapter: float(chapter.chapter_name.split(" ")[-1])
        )
        serializer = self.get_serializer(sorted_queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ChapterDetailSerializer
        return ChapterListSerializer