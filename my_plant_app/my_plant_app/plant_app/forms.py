from django import forms

from my_plant_app.plant_app.models import Profile, Plant


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('profile_picture',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantEditForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantDeleteForm(forms.ModelForm):
    class Meta:
        model = Plant
        exclude = ('pk',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Plant.objects \
                .all() \
                .delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()
