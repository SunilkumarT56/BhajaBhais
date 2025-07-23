from django.db import models


class HomeModel(models.Model):
    h_img = models.ImageField(upload_to='uploads/')
    name_img = models.CharField(max_length=100)

    def __str__(self):
        return self.name_img
class LegacyModel(models.Model):
    l_img = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=100)
    disc = models.CharField(max_length=200)

    def __str__(self):
        return self.title



