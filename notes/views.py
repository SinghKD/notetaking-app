from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class NoteCreateView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    parser_classes = (MultiPartParser, FormParser)


class NoteUpdateView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    parser_classes = (MultiPartParser, FormParser)


class NoteListView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NotePinView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def patch(self, request, *args, **kwargs):
        try:
            note = Note.objects.get(pk=kwargs.get('pk'))
        except Note.DoesNotExist:
            raise Http404("Note does not exist.")
        note.pinned = not note.pinned
        note.save()
        return Response(NoteSerializer(note).data)


class NoteDeleteView(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def delete(self, request, *args, **kwargs):
        try:
            note = Note.objects.get(pk=kwargs.get('pk'))
        except Note.DoesNotExist:
            raise Http404("Note does not exist.")
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

