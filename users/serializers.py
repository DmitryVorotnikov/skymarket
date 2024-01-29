import secrets

from rest_framework import serializers

from users.models import User
from users.services import password_hashing
from users.tasks import task_send_mail


class UserCreateUpdateForAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password_hashing(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password_hashing(validated_data)
        return super().update(instance, validated_data)


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email', 'phone', 'image',)

    def create(self, validated_data):
        password_hashing(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password_hashing(validated_data)
        return super().update(instance, validated_data)


class UserListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SendEmailSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        # Генерация случайного 10-значного токена.
        token = ''.join(secrets.choice('0123456789') for i in range(10))

        instance.token = token
        instance.save()

        user_email = instance.email

        # Вызываем асинхронную задачу для отправки письма с ссылкой и токеном.
        task_send_mail.delay(user_email=user_email, token=token)

        return {'message': 'An email with a password reset token has been sent!'}


class PasswordChangeSerializer(serializers.Serializer):
    new_password = serializers.CharField()

    def save(self, user):
        user.set_password(self.validated_data['new_password'])
        user.token = ''
        user.save()
