# nominations/serializers.py
from rest_framework import serializers
from .models import Category, Nomination

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class NominationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Nomination
        fields = ['id', 'user', 'category', 'title', 'description', 'status', 'created_at']
        read_only_fields = ['status', 'created_at', 'user']
