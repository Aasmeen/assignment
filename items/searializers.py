from rest_framework import serializers

from accounts.models import CustomUser
from items.models import Items


class BaseItemSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), write_only=True
    )

    class Meta:
        fields = ('user_id', 'name', 'price', 'selling_price')
        model = Items


class ItemsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        fields = ('user', 'name', 'price', 'selling_price')
        model = Items
    
    def get_user(self, instance):
        return instance.user.username
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class UpdateItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        user = self.context['request'].user
        if user and user.is_content_editor:
            self.fields.pop('price')

    class Meta:
        fields = ('name', 'price')
        model = Items
    
