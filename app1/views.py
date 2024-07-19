from django.shortcuts import render
from .models import info  # Make sure the model name matches the definition in models.py

def home(request):
    info_objects = info.objects.all()  # Renamed variable to avoid confusion
    context = {"info": info_objects}
    return render(request, 'home.html', context)
