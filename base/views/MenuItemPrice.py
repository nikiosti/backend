from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# BASE
from base.serializers.MenuItemPrice import MenuItemPriceSerializers
from base.models.MenuItem import MenuItemPrice
from base.permissions.MenuItemPrice import (
    CanCreateMenuItemPrice,
    CanUpdateOrDeleteMenuItemPrice,
)


class MenuItemPriceCreateView(generics.ListCreateAPIView):
    serializer_class = MenuItemPriceSerializers
    permission_classes = [
        IsAuthenticated,
        CanCreateMenuItemPrice,
    ]

    def get_queryset(self):
        return MenuItemPrice.objects.filter(owner__user=self.request.user)


class MenuItemPriceUpdateOrDeleteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemPriceSerializers
    permission_classes = [IsAuthenticated, CanUpdateOrDeleteMenuItemPrice]

    def get_queryset(self):
        return MenuItemPrice.objects.filter(owner__user=self.request.user)
