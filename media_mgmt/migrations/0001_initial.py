# Generated by Django 2.2.4 on 2020-03-09 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=255)),
                ('flickr_group_id', models.CharField(max_length=30)),
                ('photo_count', models.CharField(max_length=15)),
                ('member_count', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rm_group', to='media_mgmt.GroupMaster')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroupPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flickr_photo_id', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=255)),
                ('photo_url', models.TextField()),
                ('flickr_owner_id', models.CharField(max_length=30)),
                ('flickr_owner_name', models.CharField(max_length=100)),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rn_user_group', to='media_mgmt.UserGroup')),
            ],
        ),
    ]
