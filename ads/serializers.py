from rest_framework import serializers

from ads.models import Ad


class AdCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            'title',
            'price',
            'description',
            'image',
        )

    def create(self, validated_data):
        """ Метод укажет текущего пользователя как создателя объявления. """
        # Получаем текущего пользователя из контекста запроса.
        user = self.context['request'].user
        # Создаем объявление, указывая текущего пользователя как автора.
        ad = Ad.objects.create(user=user, **validated_data)

        return ad


class AdListRetrieveSerializer(serializers.ModelSerializer):
    user_first_name = serializers.CharField(source='user.first_name')
    user_last_name = serializers.CharField(source='user.last_name')
    user_phone = serializers.CharField(source='user.phone')

    class Meta:
        model = Ad
        fields = (
            'id',
            'title',
            'description',
            'image',
            'created_at',
            'user_first_name',
            'user_last_name',
            'user_phone',
        )
