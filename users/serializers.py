# users/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    category_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'category_id']

    def create(self, validated_data):
        category_id = validated_data.pop('category_id', None)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        # attach category to profile if provided
        if category_id:
            from nominations.models import Category
            try:
                cat = Category.objects.get(pk=category_id)
                user.profile.category = cat
                user.profile.save()
            except Category.DoesNotExist:
                pass
        return user
