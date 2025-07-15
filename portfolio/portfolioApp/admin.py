from django.contrib import admin
from .models import Message, Works

# custom admin class for the Message model
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'title')
    search_fields = ('name', 'email', 'title', 'textarea')

# custom admin class for the Works model
class WorksAdmin(admin.ModelAdmin):
    list_display = ('title', 'programing_lang_used')
    search_fields = ('title', 'programing_lang_used', 'description')

# models with their custom admin classes
admin.site.register(Message, MessageAdmin)
admin.site.register(Works, WorksAdmin)