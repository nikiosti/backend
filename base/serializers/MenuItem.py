from rest_framework import serializers

from base.models.MenuItem import MenuItem, MenuItemPrice
from base.models.Restaurateur import Restaurateur
from base.serializers.MenuItemPrice import MenuItemPriceSerializers


class MenuItemSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    prices = MenuItemPriceSerializers(many=True, required=False)

    def create(self, validated_data):
        prices = validated_data.pop("prices", [])
        menu_item = MenuItem.objects.create(**validated_data)
        for price in prices:
            MenuItemPrice.objects.create(menu_item_ref=menu_item, **price)
        return menu_item

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.image = validated_data.get("image", instance.image)
        instance.description = validated_data.get("description", instance.description)
        instance.category_ref = validated_data.get(
            "category_ref", instance.category_ref
        )

        # Получаем предоставленные в запросе цены
        prices_data = validated_data.pop("prices", [])

        # Получаем текущие цены связанные с экземпляром MenuItem
        current_prices = set(instance.prices.all())
        print(current_prices)

        # Создаем список для хранения обновленных или созданных цен
        updated_prices = []

        for price_data in prices_data:
            price_id = price_data.get("id", None)
            if price_id:
                # Если предоставлен id, обновляем существующий объект MenuItemPrice
                price_instance = MenuItemPrice.objects.get(id=price_id)

                # Обновляем данные цены
                price_instance.price = price_data.get("price", price_instance.price)
                price_instance.size_description = price_data.get(
                    "size_description", price_instance.size_description
                )
                price_instance.save()

                updated_prices.append(price_instance)
            else:
                # Если id не предоставлен, создаем новый объект MenuItemPrice
                price_instance = MenuItemPrice.objects.create(
                    menu_item_ref=instance, owner=instance.owner, **price_data
                )
                updated_prices.append(price_instance)

        # Удаляем цены, которые не были обновлены или созданы
        prices_to_delete = current_prices - set(updated_prices)
        for price_to_delete in prices_to_delete:
            price_to_delete.delete()

        # Привязываем новые или обновленные цены к экземпляру меню
        instance.prices.set(updated_prices)

        instance.save()
        return instance

    class Meta:
        model = MenuItem
        fields = "__all__"

    def validate_owner(self, value):
        restaurateur = Restaurateur.objects.get(user=value)
        return restaurateur
