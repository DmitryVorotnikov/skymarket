from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.paginators import UserPaginator
from users.permissions import IsManagerOrAdminPermission
from users.serializers import UserCreateUpdateForAdminSerializer, UserCreateUpdateSerializer, \
    UserListRetrieveSerializer, SendEmailSerializer, PasswordChangeSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    View for creating a user.
    Представление для создания пользователя.
    """

    def get_serializer_class(self):
        if not self.request.user.is_authenticated:
            return UserCreateUpdateSerializer

        elif self.request.user.is_staff:
            # Администратор может заполнять любые поля.
            return UserCreateUpdateForAdminSerializer

        elif self.request.user.role == 'MANAGER':
            # Менеджер не может создавать пользователей.
            raise PermissionDenied("Access forbidden for users with MANAGER role.")

        return UserCreateUpdateSerializer


class UserListAPIView(generics.ListAPIView):
    """
    View for viewing the list of users.
    Представление для просмотра списка пользователей.
    """
    permission_classes = [IsAuthenticated, IsManagerOrAdminPermission]
    queryset = User.objects.all()
    serializer_class = UserListRetrieveSerializer
    pagination_class = UserPaginator

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('id', 'first_name', 'last_name', 'email', 'phone',)
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone',)
    ordering_fields = ('is_active',)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    View for viewing a user.
    Представление для просмотра пользователя.
    """
    permission_classes = [IsAuthenticated, IsManagerOrAdminPermission]
    queryset = User.objects.all()
    serializer_class = UserListRetrieveSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    View for editing a user.
    Представление для редактирования пользователя.
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            # Если обычный пользователь или менеджер, то доступно только редактирование своего профиля.
            queryset = queryset.filter(id=self.request.user.id)

        return queryset

    def get_serializer_class(self):
        if self.request.user.is_staff:
            # Администратор может редактировать все поля.
            return UserCreateUpdateForAdminSerializer

        return UserCreateUpdateSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    View for deleting users. For administrators only.
    Представление для удаления пользователей. Только для администраторов.
    """
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()


class RequestChangePasswordAPIView(APIView):
    """
    View for sending an email with a token.
    Представление для отправки письма с токеном.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = SendEmailSerializer(instance=request.user)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class ChangePasswordAPIView(APIView):
    """
    Password change View.
    Представление для смены пароля.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        token_from_user = request.data.get('token_from_user')
        new_password = request.data.get('new_password')

        if token_from_user == user.token and len(new_password) >= 6:
            serializer = PasswordChangeSerializer(data={'new_password': new_password})
            if serializer.is_valid():
                serializer.save(user=user)
                return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Invalid token or new password"}, status=status.HTTP_400_BAD_REQUEST)
