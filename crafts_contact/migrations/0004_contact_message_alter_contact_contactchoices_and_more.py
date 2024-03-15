# Generated by Django 4.2 on 2024-03-15 12:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts_contact', '0003_remove_contact_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='contact',
            name='ContactChoices',
            field=models.CharField(choices=[('1', 'Business inquiries'), ('2', 'Report user'), ('3', 'Feedback about website'), ('4', 'Other questions')], default='4', max_length=1),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
