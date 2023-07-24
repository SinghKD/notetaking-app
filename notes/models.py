from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    pinned = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # for the bonus feature
    background_color = models.CharField(max_length=7, null=True, blank=True)  # for the bonus feature
