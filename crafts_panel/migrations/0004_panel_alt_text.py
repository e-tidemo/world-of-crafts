# Generated by Django 4.2 on 2024-03-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts_panel', '0003_alter_panel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='panel',
            name='alt_text',
            field=models.CharField(default='image', max_length=255),
        ),
    ]
