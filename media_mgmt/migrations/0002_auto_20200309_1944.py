# Generated by Django 2.2.4 on 2020-03-09 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media_mgmt', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rn_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupmaster',
            name='users',
            field=models.ManyToManyField(through='media_mgmt.UserGroup', to=settings.AUTH_USER_MODEL),
        ),
    ]