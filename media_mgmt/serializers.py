from rest_framework import serializers

from .models import GroupMaster, UserGroupPhoto


class GroupMasterSerializerV1(serializers.ModelSerializer):

    class Meta:
        model = GroupMaster
        fields = '__all__'


class UserGroupPhotoSerializerV1(serializers.ModelSerializer):

    class Meta:
        model = UserGroupPhoto
        fields = '__all__'
