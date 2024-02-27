from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# BASE
from base.serializers.Restaurant import RestaurantSerializers
from base.permissions.Restaurant import CanCreateRestaurant, CanUpdateOrDeleteRestaurant
from base.models.Restaurant import Restaurant


class RestaurantCreateView(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializers
    permission_classes = [IsAuthenticated, CanCreateRestaurant]

    def get_queryset(self):
        return Restaurant.objects.filter(owner__user=self.request.user)


class RestaurantUpdateOrDeleteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializers
    permission_classes = [
        IsAuthenticated,
        CanUpdateOrDeleteRestaurant,
    ]

    def get_queryset(self):
        return Restaurant.objects.filter(owner__user=self.request.user)
