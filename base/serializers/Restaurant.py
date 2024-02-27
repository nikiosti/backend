from rest_framework import serializers

# BASE
from base.models.Restaurant import Restaurant
from base.models.Restaurateur import Restaurateur


class RestaurantSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Restaurant
        fields = "__all__"

    def validate_owner(self, value):
        restaurateur = Restaurateur.objects.get(user=value)
        return restaurateur
