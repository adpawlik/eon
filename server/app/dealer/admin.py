from django.contrib import admin

from .models import Dealer

class DealerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Dealer, DealerAdmin)
