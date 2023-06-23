# Create your views here.
from django.shortcuts import render, redirect

from my_plant_app.plant_app.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from my_plant_app.plant_app.models import Profile, Plant


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()

    if profile is not None:
        return redirect('catalogue')

    context = {
        'hide_nav_links': False,
    }

    if profile is None:
        context = {
            'hide_nav_links': True,
        }

    return render(request, 'home-page.html', context)


def catalogue(request):

    plants = Plant.objects.all()

    context = {

        'plants': plants
    }

    return render(request, 'catalogue.html', context)


def profile_create(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):

    profile = get_profile()

    plants = Plant.objects.all()

    context = {
        'profile': profile,
        'plants': plants
    }

    return render(request, 'profile-details.html', context)


def profile_edit(request):

    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):

    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'delete-profile.html', context)


def plant_create(request):
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }
    return render(request, 'create-plant.html',context)


def plant_details(request, pk):

    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': plant
    }

    return render(request, 'plant-details.html', context)


def plant_edit(request, pk):

    plant = Plant.objects.filter(pk=pk).get()


    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'edit-plant.html', context)


def plant_delete(request, pk):
    plant = Plant.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:

        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'delete-plant.html', context)
