# Generated by Django 4.2 on 2024-03-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts_posts', '0002_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
