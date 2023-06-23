from django.urls import path, include

from my_plant_app.plant_app.views import index, profile_details, profile_delete, profile_edit, profile_create, \
    plant_create, plant_details, plant_edit, plant_delete, catalogue

"""

/ - home page

/catalogue/ - catalogue

/create/ - plant create page
/details/<plant_id>/ - plant details page
/edit/<plant_id>/ - plant edit page
/delete/<plant_id>/ - plant delete page



"""

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('create/', plant_create, name='plant create'),
    path('details/<int:pk>', plant_details, name='plant details'),
    path('edit/<int:pk>', plant_edit, name='plant edit'),
    path('delete/<int:pk>', plant_delete, name='plant delete'),
]
