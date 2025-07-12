from django import forms
from .models import Collage


class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class CollageForm(forms.ModelForm):
    images = forms.FileField(widget=MultiFileInput(attrs={'multiple': True}), required=True)

    class Meta:
        model = Collage
        fields = ['title', 'images']

    def clean_images(self):
        images = self.files.getlist('images')
        if len(images) < 10:
            raise forms.ValidationError("You can upload a maximum of 10 images.")
        return images

