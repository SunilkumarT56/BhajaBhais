from django.contrib import admin
from .models import HomeModel,LegacyModel,GroupModel,MemberModel

admin.site.register(HomeModel)
admin.site.register(LegacyModel)

# Register your models here.
class MemberInline(admin.TabularInline):
    model = MemberModel
    extra = 5

class GroupModelAdmin(admin.ModelAdmin):
    inlines = [MemberInline]

admin.site.register(GroupModel, GroupModelAdmin)
