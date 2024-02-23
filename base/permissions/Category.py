from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

#BASE
from base.models.Restaurateur import Restaurateur
from base.models.Restaurant import Restaurant
from base.models.Category import Category

class CanCreateCategory(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            restaurateur = get_object_or_404(Restaurateur, user = request.user)
            menu_rate_count = restaurateur.rate.count_menu

            menu_count = Category.objects.filter(owner__user = request.user).count()

            if menu_rate_count > menu_count:
                restaurant_id = request.data.get("restaurant_ref")
                restaurant = get_object_or_404(Restaurant, pk = restaurant_id)

                return restaurant.owner.user == request.user
            
            raise PermissionDenied("Превышен лимит ресторанов")
        
        return request.method == "GET"
    

class CanUpdateOrDeleteCategory(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH"]:
            restaurant_id = request.data.get("restaurant_ref")
            restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

            return restaurant.owner.user == request.user

        if request.method == "DELETE":
            return obj.owner.user == request.user

        return request.method == "GET"
