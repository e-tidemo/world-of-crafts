# Generated by Django 4.2 on 2024-03-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_rkxcnv', upload_to='images/'),
        ),
    ]