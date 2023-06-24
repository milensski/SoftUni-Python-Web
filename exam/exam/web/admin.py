from django.contrib import admin

from exam.web.models import Profile, Fruit


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    pass