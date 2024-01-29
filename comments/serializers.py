from rest_framework import serializers

from comments.models import Comment


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'ad',
            'text',
        )

    def create(self, validated_data):
        """ Метод укажет текущего пользователя как создателя комментария. """
        # Получаем текущего пользователя из контекста запроса.
        user = self.context['request'].user
        # Создаем комментарий, указывая текущего пользователя как автора.
        comment = Comment.objects.create(user=user, **validated_data)

        return comment


class CommentListSerializer(serializers.ModelSerializer):
    user_first_name = serializers.CharField(source='user.first_name')
    user_last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Comment
        fields = (
            'id',
            'ad',
            'text',
            'created_at',
            'user_first_name',
            'user_last_name',
        )
