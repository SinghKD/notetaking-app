from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO


class ModelTestCase(TestCase):
    """This class defines the test suite for the Note model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.note_title = "Write a test note"
        self.note = Note(title=self.note_title)

    def test_model_can_create_a_note(self):
        """Test the note model can create a note."""
        old_count = Note.objects.count()
        self.note.save()
        new_count = Note.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        # Create an image
        image = Image.new('RGB', (100, 100))

        # Save it into BytesIO buffer
        buffer = BytesIO()
        image.save(buffer, 'JPEG')

        self.image = SimpleUploadedFile('test.jpg', buffer.getvalue(), content_type='image/jpeg')
        self.note_data = {'title': 'Test note', 'content': 'This is a test note', 'image': self.image}
        self.response = self.client.post(
            reverse('create'),
            self.note_data,
            format="multipart"
        )

    def test_api_can_create_a_note(self):
        """Test the api has note creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertIn('image', self.response.data)

    def test_api_can_list_notes(self):
        """Test the api can get a list of notes."""
        # Create new notes
        Note.objects.create(title='Note 1', content='This is note 1')
        Note.objects.create(title='Note 2', content='This is note 2')

        # Make an API request to the list view
        response = self.client.get(
            reverse('list'), format="json"
        )

        # Check that the status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        # Check that the titles of the notes in the response match those of the notes we created
        note_titles = [note['title'] for note in response.data]
        self.assertIn('Note 1', note_titles)
        self.assertIn('Note 2', note_titles)
        self.assertIn('Test note', note_titles)


def test_api_can_update_a_note(self):
    """Test the api can update a given note."""
    # Get the created note id from the response
    note_id = self.response.data['id']

    # Define the new data for the note
    new_data = {'title': 'New Title', 'content': 'New Content'}

    # Make an API request to the update view
    response = self.client.put(
        reverse('update', kwargs={'pk': note_id}),
        new_data,
        format='json'
    )

    # Check that the status code is 200 OK
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Check that the note data was updated
    note = Note.objects.get(id=note_id)  # Get the note data from the database
    self.assertEqual(note.title, 'New Title')
    self.assertEqual(note.content, 'New Content')

    # Check that the response contains the updated note data
    response_data = response.data
    self.assertEqual(response_data['id'], note_id)
    self.assertEqual(response_data['title'], 'New Title')
    self.assertEqual(response_data['content'], 'New Content')

    def test_api_can_delete_note(self):
        """Test the api can delete a note."""
        note = Note.objects.get()
        response = self.client.delete(
            reverse('delete', kwargs={'pk': note.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_pin_note(self):
        """Test the api can pin a note."""
        note = Note.objects.get()
        response = self.client.patch(
            reverse('pin', kwargs={'pk': note.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)


class SerializerTestCase(TestCase):
    """Test suite for the note serializer."""

    def setUp(self):
        """Define the test variables."""
        self.image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.note_attributes = {'title': 'Test note', 'content': 'This is a test note', 'image': self.image}
        self.note = Note.objects.create(**self.note_attributes)
        self.serializer = NoteSerializer(instance=self.note)

    def test_contains_expected_fields(self):
        """Test that the serializer contains the expected fields."""
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         {'id', 'title', 'content', 'pinned', 'timestamp', 'background_color', 'image'})

    def test_content_field_content(self):
        """Test the content field content."""
        data = self.serializer.data
        self.assertEqual(data['title'], self.note_attributes['title'])
        self.assertEqual(data['content'], self.note_attributes['content'])

    def test_pinned_field_content(self):
        """Test the pinned field content."""
        data = self.serializer.data
        self.assertEqual(data['pinned'], False)
