from django.contrib import admin

from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'ad',
        'text',
        'created_at',
    )
    list_filter = ('user', 'ad',)
    search_fields = ('text',)
