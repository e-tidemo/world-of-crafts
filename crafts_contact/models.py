from django.db import models
from django.core.mail import send_mail
from django.conf import settings


# Some help with choices field option was collected from https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django
class Contact(models.Model):
    class ContactChoices(models.TextChoices):
        REPORT = "1", "Report user"
        BUSINESS = "2", "Business inquiries"
        FEEDBACK = "3", "Feedback about website"
        OTHER = "4", "Other questions"
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    ContactChoices = models.CharField(
        max_length=1,
        choices=ContactChoices.choices,
        default=ContactChoices.OTHER
        )
    
    def __str__(self):
        return self.name + " - " + self.subject
    
    def save(self, *args, **kwargs):
        #Send confirmation email to user
        subject = "Thank you for your email"
        message = "Thank you for contacting us. We will get back to you as soon as possible."
        sender_email = self.email
        
        send_mail(
            subject=subject,
            message=message,
            from_email=sender_email,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        super().save(*args, **kwargs)