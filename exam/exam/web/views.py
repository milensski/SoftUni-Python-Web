from django.shortcuts import render, redirect

from exam.web.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from exam.web.models import Profile, Fruit


# Create your views here.

def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):

    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'home/index.html', context)


def dashboard(request):
    profile = get_profile()
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits,
        'profile': profile
    }

    return render(request, 'home/dashboard.html', context)


def profile_create(request):

    profile = get_profile()

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):


    profile = get_profile()

    fruits = Fruit.objects.all()

    context = {
        'profile': profile,
        'fruits': fruits
    }
    return render(request, 'profile/details-profile.html', context)


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
    return render(request, 'profile/edit-profile.html',context)


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

    return render(request, 'profile/delete-profile.html', context)


def fruit_create(request):

    profile = get_profile()

    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'catalogue/create-fruit.html', context)


def fruit_details(request, pk):

    profile = get_profile()

    fruit = Fruit.objects.filter(pk=pk).get()

    context = {
        'fruit': fruit,
        'profile': profile
    }

    return render(request, 'catalogue/details-fruit.html',context)


def fruit_edit(request, pk):
    profile = get_profile()

    fruit = Fruit.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
        'profile': profile
    }
    return render(request, 'catalogue/edit-fruit.html', context)


def fruit_delete(request, pk):

    profile = get_profile()

    fruit = Fruit.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:

        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
        'profile': profile,
    }
    return render(request, 'catalogue/delete-fruit.html', context)
