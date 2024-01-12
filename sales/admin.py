from django.contrib import admin

from .models import Sale

class SalesAdmin(admin.ModelAdmin):
    list_display = ["item", "created_at", "income"]

admin.site.register(Sale, SalesAdmin)