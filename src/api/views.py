from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from account.models import Bookmark
# Create your views here.
from api.serializers import BookmarkSerializer
from api.permissions import IsOwnerOrReadOnly







class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)