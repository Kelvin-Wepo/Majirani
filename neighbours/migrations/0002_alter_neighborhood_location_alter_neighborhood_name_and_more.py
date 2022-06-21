# Generated by Django 4.0.4 on 2022-06-20 23:43

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='location',
            field=models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kisumu', 'Mombasa'), ('Mombasa', 'Mombasa')], max_length=70),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='name',
            field=models.CharField(choices=[('Juja', 'Juja'), ('Kinoo', 'Kinoo'), ('Eastleigh', 'Eastleigh'), ('Zimmerman', 'Zimmerman'), ('Ruiru', 'Ruiru'), ('Donholm', 'Donholm')], max_length=50),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('profile_photo', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]