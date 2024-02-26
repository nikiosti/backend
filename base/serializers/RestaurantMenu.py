from rest_framework import serializers
#BASE
from base.models.Category import Category
from base.models.MenuItem import MenuItem, MenuItemPrice
from base.models.Restaurant import Restaurant


class MenuItemPriceSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = MenuItemPrice
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    prices = MenuItemPriceSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()
    def get_image_url(self, obj):
        if obj.image:
            
            request = self.context.get('request')
            print(request)
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
        return None

    
    class Meta:
        model = MenuItem
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    items = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_items(self, obj):
        sorted_items = obj.items.all().order_by('-created_at')
        return MenuItemSerializer(sorted_items, many=True).data

class RestaurantMenuSerializers(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'
