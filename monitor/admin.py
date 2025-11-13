from django.contrib import admin

# Register your models here.
from .models import Alert,Client

@admin.register(Client)
class clientAdmin(admin.ModelAdmin):
    list_display = ("name","description")
    list_filter = ("name",)
    search_fields = ("name","description")

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_filter = ("status",)
    list_display = ("ip_address","ip_destination","packet_size","status")

admin.site.site_header = "nganu"

#admin.site.register(Alert)
# admin.site.register(Client)