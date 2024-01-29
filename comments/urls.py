from django.urls import path

from comments.apps import CommentsConfig
from comments.views import CommentCreateAPIView, CommentListAPIView, CommentUpdateAPIView, CommentDestroyAPIView

app_name = CommentsConfig.name

urlpatterns = [
    # URLs comment:
    path('create/', CommentCreateAPIView.as_view(), name='comments_create'),
    path('', CommentListAPIView.as_view(), name='comments_list'),  # Список комментариев.
    path('update/<int:pk>/', CommentUpdateAPIView.as_view(), name='comments_update'),
    path('delete/<int:pk>/', CommentDestroyAPIView.as_view(), name='comments_delete'),
]
