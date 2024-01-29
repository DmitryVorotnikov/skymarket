from rest_framework.permissions import BasePermission


class IsManagerOrAdminPermission(BasePermission):
    """
    Permission for an admin or manager to view users
    Разрешение админу или менеджеру на просмотр пользователей.
    """

    def has_permission(self, request, view):
        return request.user.role == 'MANAGER' or request.user.is_staff
