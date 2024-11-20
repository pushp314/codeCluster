from django.contrib import admin
from .models import *

@admin.action(description="Approve selected registrations")
def approve_registrations(modeladmin, request, queryset):
    for registration in queryset:
        if registration.status == 'Pending':
            registration.approve_registration()

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'hackerrank_id', 'status']
    list_filter = ['status']
    actions = [approve_registrations]

admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Contest)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')
    list_filter = ('submitted_at',)
