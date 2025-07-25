from django.shortcuts import render, get_object_or_404

from . models import HomeModel , LegacyModel , GroupModel , MemberModel , FacultyModel,StudentModel,SponsorsModel,ContactModel,FirstYearPhoto,SecondYearPhoto,ThirdYearPhoto,FourthYearPhoto,AllYearsPhoto

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
    data = FacultyModel.objects.all()
    return render(request , 'myapp/faculty.html',{'data':data})
def students(request):
    data = StudentModel.objects.all()
    return render(request , 'myapp/students.html',{'data':data})
def galary(request):
    data = AllYearsPhoto.objects.all()
    return render(request, 'myapp/galary.html',{'data':data})
def viewmore_galary(request):
    return render(request, 'myapp/viewmore_galary.html',{})
def sponcers(request):
    data = SponsorsModel.objects.all()
    return render(request, 'myapp/sponcers.html',{'data':data})
def js_download_page(request):
    return render(request, 'myapp/sponcers.html')
def contact(request):
    data = ContactModel.objects.filter(id=1)
    return render(request , 'myapp/contact.html',{'data':data})
def part_group(request, group_id):
    group = get_object_or_404(GroupModel, id=group_id)  # To get a single group object
    members = MemberModel.objects.filter(group=group)  # Filter members linked to that group
    return render(request, 'myapp/part_group.html', {'group': group, 'members': members})
def first(request):
    data = FirstYearPhoto.objects.all()
    return render(request , 'myapp/first.html',{'data':data})
def second(request):
    data = SecondYearPhoto.objects.all()
    return render(request , 'myapp/second.html', {'data':data})
def third(request):
    data = ThirdYearPhoto.objects.all()
    return render(request, 'myapp/third.html' , {'data':data})
def fourth(request):
    data = FourthYearPhoto.objects.all()
    return render(request,'myapp/fourth.html',{'data':data})
