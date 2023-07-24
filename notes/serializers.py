from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Note
import re


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    def validate_image(self, value):
        # Validate file type (only allow jpg, jpeg, png)
        file_type = value.content_type.split('/')[1]
        if file_type not in ['jpeg', 'jpg', 'png']:
            raise ValidationError("Invalid file type. Only 'jpg', 'jpeg', and 'png' are allowed.")

        # Validate file size (only allow files up to 2MB)
        if value.size > 2 * 1024 * 1024:
            raise ValidationError("The maximum file size that can be uploaded is 2MB")

        return value
