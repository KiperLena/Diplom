from django.db import models


class Area(models.Model):
    title = models.CharField(max_length=60)
    seria = models.CharField(max_length=20, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    otvod = models.CharField(max_length=20, blank=True, null=True)
    start = models.CharField(max_length=20, blank=True, null=True)
    stop = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)
    # description = models.TextField(blank=True, null=True)
    # area_image = models.ImageField(blank=True, null=True, upload_to='centre/%Y', default='default.jpg')
    # square = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title
