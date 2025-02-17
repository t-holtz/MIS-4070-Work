from django.urls import path

from . import views

app_name = "song"

urlpatterns = [
    path("", views.SongListView.as_view(), name="index"),

    path("<int:pk>/", views.SongDetailView.as_view(), name="detail"),

    path('create/', views.SongCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.SongUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SongDeleteView.as_view(), name='delete'),
]