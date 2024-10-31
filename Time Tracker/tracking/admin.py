from django.contrib import admin
from .models import WorkSession
from django.utils.html import format_html

class WorkSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time', 'active', 'get_screenshots')
    search_fields = ('user__username',)
    list_filter = ('active',)
    ordering = ('-start_time',)

    def get_screenshots(self, obj):
        if obj.screenshot_paths:
            links = [f'<a href="/{path}" target="_blank">{path}</a>' for path in obj.screenshot_paths]
            return format_html(', '.join(links))
        return 'No Screenshots'
    get_screenshots.short_description = 'Screenshots'

admin.site.register(WorkSession, WorkSessionAdmin)
