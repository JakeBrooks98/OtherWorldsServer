# Generated by Django 4.0.4 on 2022-06-08 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Biome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=350)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worlds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=350)),
                ('biome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='otherworldsapi.biome')),
                ('world', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='otherworldsapi.world')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=350)),
                ('date', models.CharField(max_length=20)),
                ('world', models.ManyToManyField(related_name='events', to='otherworldsapi.world')),
            ],
        ),
    ]
