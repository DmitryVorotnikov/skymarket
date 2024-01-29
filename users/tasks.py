from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def task_send_mail(user_email, token):
    """
    Отправляем пользователю письмо, с указанием токена и ссылки для смены пароля.
    """
    send_mail(
        subject='Request to change password.',
        message=f'Получен запрос на смену пароля, для смены пароля перейдите '
                f'по ссылке {settings.ALLOWED_HOSTS}/api/users/change_password/ и введите токен: {token}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
    )
