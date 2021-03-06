# Generated by Django 3.2 on 2021-04-27 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolarticlecomment',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schoolarticle',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.school'),
        ),
        migrations.AddField(
            model_name='schoolarticle',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='localarticlecomment',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='article.localarticle'),
        ),
        migrations.AddField(
            model_name='localarticlecomment',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='localarticle',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.school'),
        ),
        migrations.AddField(
            model_name='localarticle',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
