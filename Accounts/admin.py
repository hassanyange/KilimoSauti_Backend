
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = [ 'email', 'first_name', 'last_name', 'phone', 'password']
    search_fields = [ 'email', 'first_name', 'last_name', 'phone']
    filter_field = []
    # Add any other configurations or customizations as needed

admin.site.register(CustomUser, CustomUserAdmin)
