from django.contrib import admin

from my_app.my_music_app.models import Profile, Album


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass