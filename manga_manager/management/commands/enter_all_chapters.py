from typing import Any
from django.core.management import BaseCommand
from manga_manager.models import Chapter
from manga_parser import get_chapters_info_list

class Command(BaseCommand):
    help = "Commands to purse and bulk kreate all available capters"

    def handle(self, *args: Any, **options: Any) -> None:
        all_available_chapters = [
            Chapter(
                chapter_name = chapter_name,
                urls_images_list = image_urls
            )
            for chapter_name, image_urls in get_chapters_info_list()
        ]
        Chapter.objects.bulk_create(all_available_chapters)

        
        
