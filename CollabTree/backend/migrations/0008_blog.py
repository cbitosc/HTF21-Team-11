# Generated by Django 3.1.6 on 2021-04-06 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20210403_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('body', models.TextField(blank=True)),
                ('cover_image', models.ImageField(blank=True, upload_to='blog_images')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.userattribs')),
            ],
        ),
    ]
