from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Тестирование создания пользователя"""
    def test_create_user(self):
        """Создание пользователя"""
        user = User.objects.create_user('test@mail.ru', 'password123')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'test@mail.ru')

    def test_raises_error_when_no_email_is_supplied(self):
        """Проверка заполнения поля email"""
        self.assertRaises(TypeError, User.objects.create_user, email='', password='password123')

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(TypeError, 'Users must have an email address.'):
            User.objects.create_user(email='', password='password123')

    def test_raises_error_when_no_password_is_supplied(self):
        """Проверка заполнения поля password"""
        self.assertRaises(TypeError, User.objects.create_user, email='test@mail.ru', password='')

    def test_raises_error_with_message_when_no_password_is_supplied(self):
        with self.assertRaisesMessage(TypeError, 'Users must have a password.'):
            User.objects.create_user(email='test@mail.ru', password='')

    def test_create_super_user(self):
        """Создание суперпользователя"""
        user = User.objects.create_superuser('test@mail.ru', 'password123')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'test@mail.ru')
