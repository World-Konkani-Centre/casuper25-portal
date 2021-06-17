from django.contrib import admin
from .models import Testimonial, Website, Event, Banner, Visibility, Schedule, Registration


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    actions = None


@admin.register(Visibility)
class VisibilityAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'camp', 'schedule', 'teams', 'campers', 'leaderboard', 'awards', 'events')
    list_editable = ('schedule', 'teams', 'campers', 'leaderboard', 'awards', 'events')
    list_display_links = ('id', 'camp')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    actions = None


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass