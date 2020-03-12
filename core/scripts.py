import requests

from media_mgmt.models import GroupMaster, UserGroup, UserGroupPhoto


def add_flickr_groups_photos_to_db():
    data = requests.get("https://www.flickr.com/services/rest/?method=flickr.groups.pools.getGroups&api_key=392543b4e7a9d62353ff0ee0084ad1a5&format=json&nojsoncallback=1&auth_token=72157713417846451-c3c1a39587130b74&api_sig=7a78d763a2b80a47be66403f017d002f").json()

    groups = data['groups']['group']
    for group in groups:
        group_obj = GroupMaster.objects.create(flickr_group_id=group['id'],
                                               group_name=group['name'],
                                               photo_count=150,
                                               member_count=1)
        print(group['name'])

        user_group = UserGroup.objects.create(group=group_obj,
                                              user_id=1)
        url1 = f"https://www.flickr.com/services/rest/?method=flickr.groups.pools.getPhotos&api_key=e2260ba05892beafb6bf7f06b4640461&group_id={group['id'].strip()}&per_page=150&format=json&nojsoncallback=1"
        print(url1)
        data = requests.get(url1).json()
        photos = data['photos']['photo']
        for photo in photos:
            url = f"https://www.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key=e2260ba05892beafb6bf7f06b4640461&photo_id={photo['id']}&format=json&nojsoncallback=1"
            print(url)
            pic_details = requests.get(url).json()
            UserGroupPhoto.objects.create(user_group=user_group,
                                           flickr_photo_id=photo['id'],
                                           title=photo['title'],
                                           photo_url=pic_details['sizes']['size'][7],
                                           flickr_owner_id=photo['owner'],
                                           flickr_owner_name=photo['ownername']
            )

