from django.contrib import admin
from .models import About, Technologies, Team

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')

# class TecnologiesAdmin(admin.ModelAdmin):
#     readonly_fields = ('create_at', 'update_at')

# class TeamAdmin(admin.ModelAdmin):
#     readonly_fields = ('create_at', 'update_at')

admin.site.register(About, AboutAdmin)
admin.site.register(Technologies)
admin.site.register(Team)