from django.shortcuts import render

def home(request):
    return render(request,'wordcount/home.html')

def about(request):
    return render(request,'wordcount/about.html')

def count(request):
    full_text=request.GET['fulltext']
    return render(request,'wordcount/count.html',{'fulltext':full_text})   
# Create your views here.
