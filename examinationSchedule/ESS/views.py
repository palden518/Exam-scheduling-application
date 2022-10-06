from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def dashboard(request):
    return render(request, 'dashboard.html')

def examination(request):
    return render(request, 'examination.html')
def EditTimetable(request):
    return render(request, 'EditTimetable.html')
def profile(request):
    return render(request, 'profile.html')

    
    