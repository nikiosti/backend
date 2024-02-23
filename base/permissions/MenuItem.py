from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

#MODELS
from base.models.Restaurateur import Restaurateur
from base.models.MenuItem import MenuItem
from base.models.Category import Category 

class CanCreateMenuItem(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":

            restaurateur = get_object_or_404(Restaurateur, user = request.user)
            menu_item_rate_count = restaurateur.rate.count_menu_items

            menu_item_count = MenuItem.objects.filter(owner__user=request.user).count()


            if menu_item_rate_count > menu_item_count:
                category_id = request.data.get("category_ref")
                category = get_object_or_404(Category, pk=category_id)
                
                return category.owner.user == request.user
            
            raise PermissionDenied("Превышен лимит позиций")
            
        return request.method == "GET"



class CanUpdateOrDeleteMenuItem(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH"]:
            category_id = request.data.get("category_ref")
            category = get_object_or_404(Category, pk=category_id)

            return category.owner.user == request.user

        if request.method == "DELETE":
            return obj.owner.user == request.user

        return request.method == "GET"


