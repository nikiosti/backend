from rest_framework.response import Response
from rest_framework import generics

from base.serializers.Restaurateur import (
    RestaurateurSerializers,
    RestaurateurFormInLendingPageSerializer,
)
from base.models.Restaurateur import Restaurateur, RestaurateurFormInLendingPage

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated


class RestaurateurView(APIView):
    serializer_class = RestaurateurSerializers
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, *args, **kwargs):
        queryset = Restaurateur.objects.filter(user=self.request.user).first()
        serializer = self.serializer_class(
            queryset, many=False, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestaurateurFormInLendingPageView(generics.ListCreateAPIView):
    serializer_class = RestaurateurFormInLendingPageSerializer

    def get_queryset(self):
        return RestaurateurFormInLendingPage.objects.all()