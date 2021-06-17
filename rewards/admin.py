from django.contrib import admin

# Register your models here.
from rewards.models import Points, Type


@admin.register(Points)
class PointsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'points', 'heading', 'type')
    list_display_links = ('id', 'user', 'points')
    list_filter = ('camp', 'team', 'type')
    search_fields = ('user', 'team', 'heading')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass
