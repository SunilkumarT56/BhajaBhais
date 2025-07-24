from django.db import models

class HomeModel(models.Model):
    h_img = models.ImageField(upload_to='uploads/')
    name_img = models.CharField(max_length=100)

    def __str__(self):
        return self.name_img

class LegacyModel(models.Model):
    l_img = models.ImageField(upload_to='uploads/')
    title1 = models.CharField(max_length=100 , default='Untitled')
    disc1 = models.CharField(max_length = 100 , default='Untitled')
    disc2 = models.CharField(max_length = 100 , default='Untitled')
    disc3 = models.CharField(max_length = 100, default='Untitled')

    def __str__(self):
        return self.title1  # fixed here

class GroupModel(models.Model):
    p_title = models.CharField(max_length=100, default='Untitled')
    s_title = models.CharField(max_length=100, default='Untitled')
    description1 = models.TextField(default='Untitled')
    description2 = models.TextField(default='Untitled')
    description3 = models.TextField(default='Untitled')
    g_img = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.p_title

class MemberModel(models.Model):
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
 # fixed here
