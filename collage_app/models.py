from django.db import models

class Collage(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ImageItem(models.Model):
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='collages/')
