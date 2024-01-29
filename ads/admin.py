from django.contrib import admin

from ads.models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'title',
        'price',
        'description',
        'image',
        'created_at',
    )
    list_filter = ('user', 'title', 'price',)
    search_fields = ('user', 'title', 'price', 'description',)
