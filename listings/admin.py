from django.contrib import admin
from . models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'recommend', 'price', 'realtor', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'list_date', 'recommend', 'is_published')
    list_editable = ('is_published', 'recommend')
    search_fields = ('title', 'address', 'town', 'county', 'price')
    list_per_page = 25

# Register your models here.
admin.site.register(Listing, ListingAdmin)