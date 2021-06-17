from django.contrib import admin
from .models import Profile, Team, User, Camp
from django.contrib.auth.admin import UserAdmin
from csv_export.views import CSVExportView
from django.utils.html import format_html


class UserAdminClass(UserAdmin):
    @staticmethod
    def photo(obj):
        return format_html(
            '<img src="{}" width="50px" />'.format(obj.image.url))

    # list to display in admin panel
    actions = ('export_data_csv',)
    list_display = ('email', 'photo', 'name', 'batch', 'college_name')
    # search by following fields
    search_fields = ('email', 'batch', 'name', 'college_name')
    list_filter = ('profile__camps', 'batch', )
    # cannot be edited
    readonly_fields = ()

    # required features that should be overriding the UserAdmin,
    filter_horizontal = ()
    fieldsets = ()
    def export_data_csv(self, request, queryset):
        view = CSVExportView(queryset=queryset, fields='__all__')
        return view.get(request)

    export_data_csv.short_description = 'Export CSV for selected Data records'


admin.site.register(User, UserAdminClass)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_filter = ('camp', )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    @staticmethod
    def user_photo(obj):
        return format_html(
            '<img src="{}" width="40" /> <span>{}</span>'.format(obj.user.image.url, obj.user.name))

    search_fields = ('user__email', 'team__name')
    list_filter = ('camps', 'role', 'team__name')
    list_display = ('id', 'user_photo', 'role', 'team')
    list_display_links = ('id', 'user_photo')


@admin.register(Camp)
class CampAdmin(admin.ModelAdmin):
    actions = None