from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

# BASE
from base.models.Restaurateur import Restaurateur
from base.models.Restaurant import Restaurant
from rest_framework.exceptions import PermissionDenied


class CanCreateRestaurant(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":

            restaurateur = get_object_or_404(Restaurateur, user=request.user)
            restaurant_rate_count = restaurateur.rate.count_restaurants

            restaurant_count = Restaurant.objects.filter(
                owner__user=request.user
            ).count()

            if restaurant_rate_count > restaurant_count:
                return True

            raise PermissionDenied("Превышено количество ресторанов")

        return request.method == "GET"


class CanUpdateOrDeleteRestaurant(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in ["PUT", "PATCH", "DELETE"]:

            return request.user == obj.owner.user

        return request.method == "GET"
