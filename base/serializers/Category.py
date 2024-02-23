from rest_framework import serializers

#BASE
from base.models.Category import Category
from base.models.Restaurateur import Restaurateur
    

class CategorySerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = '__all__'

    def validate_owner(self, value):
        restaurateur = Restaurateur.objects.get(user=value)
        return restaurateur

