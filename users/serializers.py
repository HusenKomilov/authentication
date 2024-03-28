from rest_framework import serializers
from users import models


class UserPhoneRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=32, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=32, min_length=8, write_only=True)

    class Meta:
        model = models.User
        fields = ("full_name", "phone_number", "password1", "password2")

    def validate(self, attrs):
        password1 = attrs.get("password1", "")
        password2 = attrs.get("password2", "")
        if password1 != password2:
            raise serializers.ValidationError("1-parol va 2-parol bir xil bo'lishi kerak")
        return attrs

    def create(self, validated_data):
        user = models.User.objects.create_user_phone(
            full_name=validated_data.get('full_name'),
            phone_number=validated_data.get('phone_number'),
            password=validated_data.get("password1")
        )
        return user
