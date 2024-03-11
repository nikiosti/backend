from rest_framework import serializers

# BASE
from base.models.Restaurant import Restaurant
from base.models.Restaurateur import Restaurateur


class RestaurantSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                image_url = obj.image.url
                return request.build_absolute_uri(image_url)
        return None

    def validate_owner(self, value):
        restaurateur = Restaurateur.objects.get(user=value)
        return restaurateur

    class Meta:
        model = Restaurant
        fields = "__all__"
