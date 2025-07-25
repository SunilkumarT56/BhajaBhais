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
class FacultyModel(models.Model):
    f_img = models.ImageField(upload_to='uploads/')
    f_name =  models.CharField(max_length=100 , default='Untitled')
    f_title = models.CharField(max_length=100, default='Untitled')

    def __str__(self):
        return self.f_name
class StudentModel(models.Model):
    s_img = models.ImageField(upload_to='uploads/')
    s_name =  models.CharField(max_length=100 , default='Untitled')
    s_title = models.CharField(max_length=100, default='Untitled')

    def __str__(self):
        return self.s_name
class SponsorsModel(models.Model):
    gold_img = models.ImageField(upload_to='uploads/')
    other_img = models.ImageField(upload_to='uploads/')
    prev_img = models.ImageField(upload_to='uploads/')


class ContactModel(models.Model):
    phone_number = models.CharField(max_length=15, help_text="Enter phone number with country code, e.g. +91XXXXXXXXXX")
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.email} - {self.phone_number}"
    
from django.db import models

# Separate models for each year
class FirstYearPhoto(models.Model):
    title = models.CharField(max_length=100)
    row1 = models.ImageField(upload_to='uploads/')
    row2 = models.ImageField(upload_to='uploads/')
    row3 = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SecondYearPhoto(models.Model):
    title = models.CharField(max_length=100)
    row1 = models.ImageField(upload_to='uploads/')
    row2 = models.ImageField(upload_to='uploads/')
    row3 = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ThirdYearPhoto(models.Model):
    title = models.CharField(max_length=100)
    row1 = models.ImageField(upload_to='uploads/')
    row2 = models.ImageField(upload_to='uploads/')
    row3 = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FourthYearPhoto(models.Model):
    title = models.CharField(max_length=100)
    row1 = models.ImageField(upload_to='uploads/')
    row2 = models.ImageField(upload_to='uploads/')
    row3 = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class BaseYearPhoto(models.Model):
    title = models.CharField(max_length=100)
    row1 = models.ImageField(upload_to='uploads/')
    row2 = models.ImageField(upload_to='uploads/')
    row3 = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # Doesn't create a separate DB table



class FirstYearPhoto(BaseYearPhoto):
    pass

class SecondYearPhoto(BaseYearPhoto):
    pass

class ThirdYearPhoto(BaseYearPhoto):
    pass

class FourthYearPhoto(BaseYearPhoto):
    pass
class AllYearsPhoto(BaseYearPhoto):
    YEAR_CHOICES = [
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    ]
    year = models.CharField(max_length=1, choices=YEAR_CHOICES)

    def __str__(self):
        return f"{self.get_year_display()} - {self.title}"
