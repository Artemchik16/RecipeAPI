from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext as _


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'phone_number', 'last_name', 'first_name',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5
            },
        }

        def create(self, validated_data):
            return get_user_model().objects.create_user(**validated_data)

        def update(self, instance, validated_data):
            password = validated_data.pop('password', None)
            user = super().update(instance, validated_data)

            if password:
                user.set_password(password)
                user.save()

            return user


class AuthTokenSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=16)
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=phone_number,
            password=password,
        )

        if not user:
            raise serializers.ValidationError('Error', code='authorization')

        attrs['user'] = user

        return attrs
