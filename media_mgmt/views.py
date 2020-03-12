from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import GroupMaster, UserGroupPhoto
from .serializers import GroupMasterSerializerV1, UserGroupPhotoSerializerV1


@api_view(['GET'])
def user_group(request, version, group_id=None):
    try:
        user = request.user
        if group_id is None:
            groups = GroupMaster.objects.filter(users=user)
            paginator = PageNumberPagination()
            results = paginator.paginate_queryset(groups, request)
            group_serializer = GroupMasterSerializerV1(results, many=True)
            return paginator.get_paginated_response(group_serializer.data)
        else:
            if not GroupMaster.objects.filter(users=user,
                                              id=group_id).exists():  # Check user belongs to the given group
                return Response({'success': False,
                                 "error": {
                                     "code": 405,
                                     "message": 'User not belongs to this group.'
                                 }},
                                status=status.HTTP_405_METHOD_NOT_ALLOWED)
            group_photos = UserGroupPhoto.objects.filter(user_group__user=user, user_group__group=group_id)
            paginator = PageNumberPagination()
            results = paginator.paginate_queryset(group_photos, request)
            group_serializer = UserGroupPhotoSerializerV1(results, many=True)
            return paginator.get_paginated_response(group_serializer.data)
    except Exception as e:
        return Response({'success': False,
                         "error": {
                             "code": e.code,
                             "message": e.detail
                         }}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_group_photos(request, version, photo_id=None):
    try:
        user = request.user
        if photo_id is None:
            group_id = request.GET.get('group', None)
            if group_id is None:
                return Response({'success': False,
                                 "error": {
                                     "code": 400,
                                     "message": 'No parameters provided.'
                                 }},
                                status=status.HTTP_400_BAD_REQUEST)
            if not GroupMaster.objects.filter(users=user,
                                              id=group_id).exists():  # Check user belongs to the given group
                return Response({'success': False,
                                 "error": {
                                     "code": 405,
                                     "message": 'User not belongs to this group.'
                                 }},
                                status=status.HTTP_405_METHOD_NOT_ALLOWED)
            group_photos = UserGroupPhoto.objects.filter(user_group__user=user, user_group__group=group_id)
            paginator = PageNumberPagination()
            results = paginator.paginate_queryset(group_photos, request)
            group_serializer = UserGroupPhotoSerializerV1(results, many=True)
            return paginator.get_paginated_response(group_serializer.data)
        else:
            if not GroupMaster.objects.filter(users=user,
                                              rn_group__rn_user_group__id=photo_id).exists():   # Check user belongs to the group of given photo_id
                return Response({'success': False,
                                 "error": {
                                     "code": 405,
                                     "message": 'User not belongs to this group.'
                                 }},
                                status=status.HTTP_405_METHOD_NOT_ALLOWED)
            group_photo = UserGroupPhoto.objects.get(user_group__user=user, id=photo_id)
            group_serializer = UserGroupPhotoSerializerV1(group_photo)
            return Response({'success': True,
                             'details': {
                                 'message': 'Details of given photo.',
                                 'data': group_serializer.data,
                             }},
                            status=status.HTTP_200_OK)
    except UserGroupPhoto.DoesNotExist:
        return Response({'success': False,
                         "error": {
                             "code": 404,
                             "message": 'Photo not found.'
                         }}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'success': False,
                         "error": {
                             "code": e.code,
                             "message": e.detail
                         }}, status=status.HTTP_400_BAD_REQUEST)

