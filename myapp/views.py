from django.shortcuts import render, get_object_or_404

from . models import HomeModel , LegacyModel , GroupModel , MemberModel


def home(request):
    data = HomeModel.objects.all()
    return render(request , 'myapp/home.html' , {'data':data})
def legacy(request):
    data = LegacyModel.objects.all()
    return render(request , 'myapp/legacy.html',{'data':data})
def legacy_more(request):
    data = GroupModel.objects.all()
    return render(request,'myapp/legacy_more.html',{'data': data})
def particular_legacy(request,legacy_id):
    data = LegacyModel.objects.filter(id=legacy_id)
    return render(request , 'myapp/particular_legacy.html' , {'data':data})
def faculty(request):
    return render(request , 'myapp/faculty.html',{})
def students(request):
    return render(request , 'myapp/students.html',{})
def galary(request):
    return render(request, 'myapp/galary.html',{})
def viewmore_galary(request):
    return render(request, 'myapp/viewmore_galary.html',{})
def sponcers(request):
    return render(request, 'myapp/sponcers.html',{})
def js_download_page(request):
    return render(request, 'myapp/sponcers.html')
def contact(request):
    return render(request , 'myapp/contact.html',{})
def part_group(request, group_id):
    group = get_object_or_404(GroupModel, id=group_id)  # To get a single group object
    members = MemberModel.objects.filter(group=group)  # Filter members linked to that group
    return render(request, 'myapp/part_group.html', {'group': group, 'members': members})
