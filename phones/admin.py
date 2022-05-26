from django.contrib import admin
from jmespath import search
from .models import Phone

class PhonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'release_date', 'lte_exists')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price')
admin.site.register(Phone, PhonesAdmin)