from django.urls import path
from .views import NoteCreateView, NoteListView, NotePinView, NoteDeleteView, NoteUpdateView

urlpatterns = [
    path('create/', NoteCreateView.as_view(), name='create'),
    path('list/', NoteListView.as_view(), name='list'),
    path('pin/<int:pk>/', NotePinView.as_view(), name='pin'),
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', NoteUpdateView.as_view(), name='update'),
]
