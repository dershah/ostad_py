from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }   


    def create(self, validated_data):
        password = validated_data.pop('password', None) #extracting the password from validated_data
        user = CustomUser(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user