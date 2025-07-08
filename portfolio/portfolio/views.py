from django.shortcuts import render


def index(request):
    """
    Render the index page.
    This function handles the request to the index page and returns the rendered HTML template.
    """
    return render(request, 'index.html')