from account.models import Bookmark
from rest_framework import serializers




class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Bookmark
        fields = ('user','owner', 'url','title', 'description', 'user')
