from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('title', 'creation_date')

    fieldsets = (
        ('Main', {
            'fields': (
                'title',
                'creation_date')
        }),
    )
