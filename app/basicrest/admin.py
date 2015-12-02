from django.contrib import admin
from models import *
from django.contrib.admin import TabularInline, StackedInline, site
import locale
import pytz
from datetime import datetime


class PetActivityInline(TabularInline):
    model = PetActivity
    readonly_fields = ('date', 'activity',)
    verbose_name_plural = "Activities"

    def get_fecha(self, obj):
        return obj.date.astimezone(pytz.timezone('America/Guayaquil')).strftime('%d/%m/%Y at %H:%M:%S')

    get_fecha.short_description = 'Date'

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class PetAdmin(admin.ModelAdmin):
    inlines = [PetActivityInline]
    search_fields = ['name', 'race', 'creation_date']
    list_display = ['creation_date', 'name', 'race']


admin.site.register(Pet, PetAdmin)
