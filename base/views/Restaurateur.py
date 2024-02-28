# REST
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from base.serializers.Restaurateur import RestaurateurSerializers
from base.models.Restaurateur import Restaurateur

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RestaurateurView(APIView):
    serializer_class = RestaurateurSerializers

    def get(self, request, *args, **kwargs):
        queryset = Restaurateur.objects.filter(user=self.request.user).first()
        serializer = self.serializer_class(
            queryset, many=False, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
