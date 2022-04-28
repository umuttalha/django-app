from django.contrib import admin
from jmespath import search

from .models import Information
# Register your models here.

@admin.register(Information)
class InfoAdmin(admin.ModelAdmin):
    
    list_display = ["author", "title", "created_date"]
    list_display_links = ['author', 'title']
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Information
