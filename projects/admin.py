from django.contrib import admin
from projects.models import Project, LandingMessage
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Project, ProjectAdmin)
admin.site.register(LandingMessage)