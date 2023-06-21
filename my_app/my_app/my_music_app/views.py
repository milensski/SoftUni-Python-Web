from django.shortcuts import render, redirect

from my_app.my_music_app.forms import ProfileCreateForm, AlbumCreateForm
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

    context = {
        'form': form,

    }


    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    pass


def edit_album(request, pk):
    pass


def delete_album(request, pk):
    pass


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

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
    return render(request, 'profile/profile-details.html')


def profile_delete(request):
    pass
