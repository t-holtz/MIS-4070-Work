from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from songs.models import Song
from songs.forms import SongCreateForm


class SongListView(ListView):
    model = Song
    template_name = 'song_index.html'
    context_object_name = 'songs'


class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'


class SongCreateView(CreateView):
    template_name = 'song_create_form.html'
    form_class = SongCreateForm

class SongUpdateView(UpdateView):
    model = Song
    fields = "__all__"
    template_name = 'song_update_form.html'


class SongDeleteView(DeleteView):
    model = Song
    template_name = 'song_confirm_delete.html'
    success_url = reverse_lazy("song:index")
