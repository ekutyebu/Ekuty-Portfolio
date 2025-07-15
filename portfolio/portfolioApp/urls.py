from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('process_form/', views.process_form, name='process_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)