# Generated by Django 4.0.3 on 2022-03-27 04:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('contributors', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('source_code', models.URLField(blank=True, null=True)),
                ('vote_total', models.IntegerField(default=0)),
                ('vote_ratio', models.IntegerField(default=0)),
                ('date_started', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.project')),
            ],
        ),
    ]