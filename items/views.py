from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from items.constants import CONTENT_WRITTER_UPDATE_FIELDS
from items.models import Items
from items.permissions import CanCreateorDeleteItem, CanUpdateItem
from items.searializers import ItemsSerializer, UpdateItemSerializer


class CreateItemAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, CanCreateorDeleteItem]
    serializer_class = ItemsSerializer


class GetItemAPIView(RetrieveAPIView):
    queryset = Items.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ItemsSerializer


class ListItemsAPIView(ListAPIView):
    queryset = Items.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ItemsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'user__username']


class UpdateItemAPIView(UpdateAPIView):
    method_allowed = ['patch']
    queryset = Items.objects.all()
    permission_classes = [IsAuthenticated, CanUpdateItem]
    serializer_class = UpdateItemSerializer

    def update(self, request, *args, **kwargs):
        user = request.user
        if user.is_content_editor and set(request.data.keys()) - CONTENT_WRITTER_UPDATE_FIELDS:
            raise ValidationError("Content Editors can only update the 'name' field.")
        return super().update(request, *args, **kwargs)


class DeleteItemAPIView(DestroyAPIView):
    queryset = Items.objects.all()
    permission_classes = [IsAuthenticated, CanCreateorDeleteItem]
    serializer_class = ItemsSerializer
