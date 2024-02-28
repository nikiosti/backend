from rest_framework import serializers
from base.models.Restaurateur import Restaurateur
from base.serializers.Rate import RateSerializers


class RestaurateurSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    rate = RateSerializers()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Restaurateur
        fields = "__all__"

    def validate_owner(self, value):
        restaurateur = Restaurateur.objects.get(user=value)
        return restaurateur

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                image_url = obj.image.url
                return request.build_absolute_uri(image_url)
        return None