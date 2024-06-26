from rest_framework import serializers
from base.models.Restaurateur import Restaurateur, RestaurateurFormInLendingPage
from base.serializers.Rate import RateSerializers


class RestaurateurSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    rate = RateSerializers()

    class Meta:
        model = Restaurateur
        fields = "__all__"

    def validate_owner(self, value):
        restaurateur = Restaurateur.objects.get(user=value)
        return restaurateur


class RestaurateurFormInLendingPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurateurFormInLendingPage
        fields = "__all__"
