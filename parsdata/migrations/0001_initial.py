# Generated by Django 4.0.3 on 2022-03-22 15:28

from django.db import migrations, models
import django.db.models.deletion
import parsdata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFromParser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('parsedtext', models.TextField(max_length=5000, null=True)),
                ('parsedjson', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageFromParser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='parsdata.datafromparser')),
            ],
        ),
    ]
