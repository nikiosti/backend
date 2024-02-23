from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

#MODELS
from base.models.MenuItem import MenuItem


class CanCreateMenuItemPrice(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            menu_item_id = request.data.get("menu_item_ref")
            menu_item = get_object_or_404(MenuItem, pk=menu_item_id)

            return menu_item.owner.user == request.user
            
        return request.method == "GET"



class CanUpdateOrDeleteMenuItemPrice(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH"]:
            menu_item_id = request.data.get("menu_item_ref")
            menu_item = get_object_or_404(MenuItem, pk=menu_item_id)

            return menu_item.owner.user == request.user

        if request.method == "DELETE":
            return obj.owner.user == request.user

        return request.method == "GET"


