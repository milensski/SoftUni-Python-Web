from django.shortcuts import render, redirect

from my_app.my_music_app.forms import ProfileCreateForm, AlbumCreateForm, AlbumDeleteForm, ProfileDeleteForm
from my_app.my_music_app.models import Profile, Album


# Create your views here.

def get_profile():
    try:
        return Profile.objects.first()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()

    if profile is None:
        return add_profile(request)

    context = {
        'albums': Album.objects.all(),
    }

    return render(
        request,
        'home/home-with-profile.html',
        context,
    )


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    print(form)

    context = {
        'form': form,

    }

    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        'album': album
    }

    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = AlbumCreateForm(instance=album)
    else:
        form = AlbumCreateForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album
    }

    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album
    }

    return render(request, 'album/delete-album.html', context)


def add_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(request, 'home/home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()

    count_albums = Album.objects.all().count()

    context = {
        'profile': profile,
        'count_albums': count_albums
    }

    return render(request, 'profile/profile-details.html', context)


def profile_delete(request):
    profile = get_profile()

    print(profile)

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-delete.html', context)


def about(request):

    context = {
        'hide_nav_links': True
    }

    return render(request, 'about.html', context)
