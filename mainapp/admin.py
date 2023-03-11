from django.contrib import admin
from django.utils.html import format_html

from mainapp.models import News, Course, Lesson, CourseTeacher

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseTeacher)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'deleted',
        'slug'
    )
    ordering = ('pk',)
    list_per_page = 20
    list_filter = ('deleted', 'created_at',)
    search_fields = ('title', 'preamble', 'body',)
    actions = ('mark_as_deleted',)

    def slug(self, obj):
        return format_html(
            '<a href ="{}" target="_blank">{}</a>',
            obj.title.lower().replace(' ', '-'),
            obj.title
        )

    slug.short_description = 'СЛАГ'

    def mark_as_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_deleted.short_description = 'Пометить удаленными'
