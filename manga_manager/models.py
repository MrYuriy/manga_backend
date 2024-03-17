from django.db import models

class Chapter(models.Model):
    chapter_name = models.CharField(max_length=100)
    urls_images_list = models.JSONField()

    def __str__(self):
        return self.chapter_name
    