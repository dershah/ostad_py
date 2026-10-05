from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'password',
            'created_at', 'updated_at']
        extra_kwargs = {
            'is_staff': {'read_only': True},
            'password': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def __init__(self, *args, **kwargs):#
        super().__init__(*args, **kwargs)
        if self.context.get('request') and self.context['request'].method == 'POST':
            self.fields['password'].required = True
        else:
            self.fields['password'].required = False

    def create(self, validated_data):
        password = validated_data.pop('password', None) #extracting the password from validated_data
        user = CustomUser(**validated_data)
        if password is not None:
            user.set_password(password)
            user.save()
        return user