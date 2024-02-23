from rest_framework import serializers
from base.models.MenuItem import MenuItemPrice

from base.models.Restaurateur import Restaurateur

class MenuItemPriceSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    id = serializers.UUIDField(required=False)
    class Meta:
        model = MenuItemPrice
        fields = "__all__"
        read_only_fields = ('menu_item_ref',)



    def validate_owner(self, value):
        restaurateur = Restaurateur.objects.get(user=value)
        return restaurateur