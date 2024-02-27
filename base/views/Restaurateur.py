# REST
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from base.serializers.Restaurateur import RestaurateurSerializers
from base.models.Restaurateur import Restaurateur


class RestaurateurView(generics.ListAPIView):
    serializer_class = RestaurateurSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return Restaurateur.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset.first())
        return Response(serializer.data)
