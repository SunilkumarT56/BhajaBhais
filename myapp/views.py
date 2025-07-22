from django.shortcuts import render


def home(request):
    return render(request , 'myapp/home.html' , {})
def legacy(request):
    return render(request , 'myapp/legacy.html',{})
def legacy_more(request):
    return render(request,'myapp/legacy_more.html',{})
def particular_legacy(request):
    return render(request , 'myapp/particular_legacy.html' , {})
def faculty(request):
    return render(request , 'myapp/faculty.html',{})
def students(request):
    return render(request , 'myapp/students.html',{})
def galary(request):
    return render(request, 'myapp/galary.html',{})
def viewmore_galary(request):
    return render(request, 'myapp/viewmore_galary.html',{})