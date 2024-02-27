from rest_framework import generics
from base.models.Restaurant import Restaurant

from base.serializers.RestaurantMenu import RestaurantMenuSerializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RestaurantMenuView(APIView):
    serializer_class = RestaurantMenuSerializers

    def get(self, request, *args, **kwargs):
        queryset = Restaurant.objects.filter(owner__user=request.user)
        serializer = self.serializer_class(queryset, many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class RestaurantMenuUserView(generics.RetrieveAPIView):
    serializer_class = RestaurantMenuSerializers
    queryset = Restaurant.objects.all()
