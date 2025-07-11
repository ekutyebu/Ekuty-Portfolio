from django.shortcuts import render
from .models import Works

# Create your views here.
def index(request):
    """
    Render the index page.
    This function handles the request to the index page and returns the rendered HTML template.
    """
    projects = Works.objects.all()
    return render(request, 'index.html', {'projects': projects})