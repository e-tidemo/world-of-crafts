from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Panel(models.Model):
    # For the admins to share tips and resources to the site users
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, unique=True, blank=False)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    alt_text = models.CharField(max_length=255, blank=False)
    video_url = models.URLField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
    
    def clean(self):
        if not self.content and not self.image and not self.video_url:
            raise ValidationError("At least one of 'content', 'image', or 'video_url' must be provided.")