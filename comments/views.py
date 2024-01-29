from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from comments.paginators import CommentPaginator
from comments.permissions import IsOwnerOrManagerOrAdmin
from comments.serializers import CommentCreateUpdateSerializer, CommentListSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    """
    View for creating a comment.
    Представление для создания комментария.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateUpdateSerializer


class CommentListAPIView(generics.ListAPIView):
    """
    View for viewing the list of comments.
    Представление для просмотра списка комментариев.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CommentListSerializer
    pagination_class = CommentPaginator
    queryset = Comment.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('text', 'created_at',)
    search_fields = ('text',)
    ordering_fields = ('ad',)


class CommentUpdateAPIView(generics.UpdateAPIView):
    """
    View for editing a comment.
    Представление для редактирования комментария.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrManagerOrAdmin]
    serializer_class = CommentCreateUpdateSerializer
    queryset = Comment.objects.all()


class CommentDestroyAPIView(generics.DestroyAPIView):
    """
    View for deleting a comment.
    Представление для удаления комментария.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrManagerOrAdmin]
    queryset = Comment.objects.all()
