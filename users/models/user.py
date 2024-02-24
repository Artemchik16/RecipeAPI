from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from users.models.user_manager import CustomUserManager


class User(AbstractUser):
    phone_number = PhoneNumberField(
        verbose_name='Phone number', unique=True, max_length=16
    )

    USERNAME_FIELD = 'phone_number'

    objects = CustomUserManager()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.id} - {self.username}'
