from rest_framework import generics
from base.models.Restaurant import Restaurant

from base.serializers.RestaurantMenu import RestaurantMenuSerializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RestaurantMenuView(generics.RetrieveAPIView):
    serializer_class = RestaurantMenuSerializers
    def get_queryset(self):
        return Restaurant.objects.filter(owner__user=self.request.user)


class RestaurantMenuUserView(generics.RetrieveAPIView):
    serializer_class = RestaurantMenuSerializers
    queryset = Restaurant.objects.all()
