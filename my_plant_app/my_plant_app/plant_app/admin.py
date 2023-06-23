from django.contrib import admin

from my_plant_app.plant_app.models import Profile, Plant


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass
