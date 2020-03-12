from django.db import models

# Create your models here.

from user_mgmt.models import UserMaster


class GroupMaster(models.Model):
    group_name = models.CharField(max_length=255)
    flickr_group_id = models.CharField(max_length=30)
    photo_count = models.CharField(max_length=15)
    member_count = models.CharField(max_length=15)
    users = models.ManyToManyField(UserMaster, through='UserGroup')

    def __str__(self):
        return "%s. %s" % (self.id, self.group_name)


class UserGroup(models.Model):
    group = models.ForeignKey(GroupMaster, on_delete=models.SET_NULL, null=True, related_name='rn_group')
    user = models.ForeignKey(UserMaster, on_delete=models.CASCADE, related_name='rn_user')

    def __str__(self):
        return "%s - %s" % (self.group, self.user)


class UserGroupPhoto(models.Model):
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, related_name='rn_user_group')
    flickr_photo_id = models.CharField(max_length=30)
    title = models.CharField(max_length=255)
    photo_url = models.TextField()
    flickr_owner_id = models.CharField(max_length=30)
    flickr_owner_name = models.CharField(max_length=100)
