from rest_framework import serializers
from .models import User

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    # Password field is write-only (will not be returned in API responses)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User  # Model to serialize
        fields = ('email', 'password')  # Fields to expose

    # Overriding create method to use custom create_user (handles password hashing)
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# Serializer for user login
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
