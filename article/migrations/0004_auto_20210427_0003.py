# Generated by Django 3.2 on 2021-04-27 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_localarticlecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='localarticle',
            name='created_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='schoolarticle',
            name='created_at',
            field=models.DateTimeField(default=None),
        ),
    ]
