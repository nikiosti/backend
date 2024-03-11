from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

# BASE
from base.models.MenuItem import MenuItem
from base.permissions.MenuItem import CanCreateMenuItem, CanUpdateOrDeleteMenuItem
from base.serializers.MenuItem import MenuItemSerializers


class MenuItemCreateView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = MenuItemSerializers
    permission_classes = [IsAuthenticated, CanCreateMenuItem]

    def get_queryset(self):
        return MenuItem.objects.filter(owner__user=self.request.user)


class MenuItemUpdateOrDeleteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemSerializers
    permission_classes = [IsAuthenticated, CanUpdateOrDeleteMenuItem]

    def get_queryset(self):
        return MenuItem.objects.filter(owner__user=self.request.user)
