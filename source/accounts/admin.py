from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import User
from .models import Profile, Team


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['avatar', 'about_me', 'git_http']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
admin.site.register(Team)