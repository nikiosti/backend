from django.urls import path

# VIEWS
from rest_framework_simplejwt.views import TokenRefreshView

# BASE VIEWS
from base.views.Token import UserTokenObtainPairView
from base.views.Restaurant import (
    RestaurantCreateView,
    RestaurantUpdateOrDeleteDetailView,
)
from base.views.Category import CategoryCreateView, CategoryUpdateOrDeleteDetailView
from base.views.MenuItem import MenuItemCreateView, MenuItemUpdateOrDeleteDetailView
from base.views.MenuItemPrice import (
    MenuItemPriceCreateView,
    MenuItemPriceUpdateOrDeleteDetailView,
)
from base.views.Restaurateur import RestaurateurView, RestaurateurFormInLendingPageView
from base.views.RestaurantMenu import RestaurantMenuView, RestaurantMenuUserView


urlpatterns = [
    path("token/", UserTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("restaurants/", RestaurantCreateView.as_view()),
    path("restaurants/<uuid:pk>/", RestaurantUpdateOrDeleteDetailView.as_view()),
    path("category/", CategoryCreateView.as_view()),
    path("category/<uuid:pk>/", CategoryUpdateOrDeleteDetailView.as_view()),
    path("menu_item/", MenuItemCreateView.as_view()),
    path("menu_item/<uuid:pk>/", MenuItemUpdateOrDeleteDetailView.as_view()),
    path("menu_item_price/", MenuItemPriceCreateView.as_view()),
    path("menu_item_price/<uuid:pk>/", MenuItemPriceUpdateOrDeleteDetailView.as_view()),
    path("restaurateur/", RestaurateurView.as_view()),
    path("restaurant_menu/<uuid:pk>/", RestaurantMenuView.as_view()),
    path("restaurant_user_menu/<uuid:pk>/", RestaurantMenuUserView.as_view()),
    path("bid/", RestaurateurFormInLendingPageView.as_view()),
]
