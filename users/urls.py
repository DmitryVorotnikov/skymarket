from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    RequestChangePasswordAPIView, ChangePasswordAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='users_create'),  # Регистрация пользователя.
    path('', UserListAPIView.as_view(), name='users_list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='users_get'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='users_update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='users_delete'),

    # Запрос на изменение пароля
    path('request_change_password/', RequestChangePasswordAPIView.as_view(), name='request_change_password'),
    # Изменение пароля
    path('change_password/', ChangePasswordAPIView.as_view(), name='change_password'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Авторизация пользователя.
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
