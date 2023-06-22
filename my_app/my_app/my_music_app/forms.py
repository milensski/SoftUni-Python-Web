from django import forms

from my_app.my_music_app.models import Profile, Album


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                }
            ),
        }


class ProfileDeleteForm(ProfileCreateForm):

    class Meta:
        model = Profile
        fields = ()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            Album.objects \
                .all() \
                .delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'genre': forms.Select(
                attrs={
                    'placeholder': 'Genre',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class AlbumDeleteForm(AlbumCreateForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
