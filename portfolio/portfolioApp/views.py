from django.shortcuts import render, redirect
from .models import Works, Message

# Create your views here
        
def index(request):
    """
    Render the index page.
    This function handles the request to the index page and returns the rendered HTML template.
    """
    projects = Works.objects.all()
    return render(request, 'index.html', {'projects': projects})

# myapp/views.py
def process_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        form_message = request.POST.get('message')

        # --- VALIDATION ---
        if name and email and form_message:
            Message.objects.create(
                name=name,
                email=email,
                title=title,
                textarea=form_message
            )
            return redirect('index')
        else:

            return redirect('index')

    return redirect('index')