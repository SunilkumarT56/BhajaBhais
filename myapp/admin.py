from django.contrib import admin
from .models import HomeModel,LegacyModel,GroupModel,MemberModel,FacultyModel,StudentModel,SponsorsModel,ContactModel,FirstYearPhoto,SecondYearPhoto,ThirdYearPhoto,FourthYearPhoto,BaseYearPhoto,AllYearsPhoto

admin.site.register(HomeModel)
admin.site.register(LegacyModel)
admin.site.register(FacultyModel)
admin.site.register(StudentModel)
admin.site.register(ContactModel)
admin.site.register(SponsorsModel)
admin.site.register(FirstYearPhoto)
admin.site.register(SecondYearPhoto)
admin.site.register(ThirdYearPhoto)
admin.site.register(FourthYearPhoto)
admin.site.register(AllYearsPhoto)


# Register your models here.
class MemberInline(admin.TabularInline):
    model = MemberModel
    extra = 5

class GroupModelAdmin(admin.ModelAdmin):
    inlines = [MemberInline]

admin.site.register(GroupModel, GroupModelAdmin)
