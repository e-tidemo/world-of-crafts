from django.db import models
from django.contrib.auth.models import User
from crafts_posts.models import Post
from django.core.validators import MinLengthValidator


class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=1100, null=False, blank=False)

    class Meta:
        ordering = ['-created_at']

    variable = models.TextField(
        validators=[
            MinLengthValidator(50, 'the field must contain at least 50 characters')
            ]
        )

    def __str__(self):
        return self.content