# Generated by Django 3.0.6 on 2020-06-12 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('repository', models.CharField(max_length=100)),
                ('technologies_used', models.CharField(max_length=50)),
                ('live_link', models.URLField()),
            ],
        ),
    ]
