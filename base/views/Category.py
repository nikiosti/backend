from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from base.serializers.Category import CategorySerializers
from base.permissions.Category import CanCreateCategory, CanUpdateOrDeleteCategory
from base.models.Category import Category


class CategoryCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializers
    permission_classes = [
        IsAuthenticated,
        CanCreateCategory,
    ]

    def get_queryset(self):
        return Category.objects.filter(owner__user=self.request.user)


class CategoryUpdateOrDeleteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializers
    permission_classes = [
        IsAuthenticated,
        CanUpdateOrDeleteCategory,
    ]

    def get_queryset(self):
        return Category.objects.filter(owner__user=self.request.user)
