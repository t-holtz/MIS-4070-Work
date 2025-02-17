from django import forms
from songs.models import Song

class SongCreateForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
