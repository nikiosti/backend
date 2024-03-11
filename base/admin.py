from django.contrib import admin

from base.models.Rate import Rate
from base.models.Restaurateur import Restaurateur, RestaurateurFormInLendingPage
from base.models.Restaurant import Restaurant
from base.models.Category import Category
from base.models.MenuItem import MenuItem, MenuItemPrice


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass


@admin.register(Restaurateur)
class RestaurateurAdmin(admin.ModelAdmin):
    pass


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(MenuItemPrice)
class MenuItemPriceAdmin(admin.ModelAdmin):
    list_display = ("id", "size_description")


@admin.register(RestaurateurFormInLendingPage)
class RestaurateurFormInLendingPageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phoneOrMessenger")