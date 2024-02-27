from rest_framework import serializers
from base.models.Rate import Rate

from base.models.Restaurateur import Restaurateur


class RateSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rate
        fields = "__all__"

    def validate_owner(self, value):
        restaurateur = Restaurateur.objects.get(user=value)
        return restaurateur
