# Generated by Django 4.0.3 on 2022-03-22 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parsdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafromparser',
            name='author',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='datafromparser',
            name='parsedjson',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datafromparser',
            name='parsedtext',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
