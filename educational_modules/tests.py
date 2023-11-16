from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from educational_modules.models import Module
from users.models import User


class ModuleTestCase(APITestCase):
    """Тестирование CRUD"""

    def setUp(self) -> None:
        """Подготовка данных для тестирования"""

        self.user = User.objects.create(email='test0@mail.ru', is_staff=True, is_superuser=True)
        self.client.force_authenticate(self.user)
        self.module = Module.objects.create(title='test', owner=self.user)

    def test_list_module(self):
        """Тестирование вывода списка модулей"""
        response = self.client.get(reverse('educational_modules:module_list'))

        # Проверяем статус вывода списка
        self.assertEquals(response.status_code,
                          status.HTTP_200_OK)

        #  Проверка корректности данных
        self.assertEquals(response.json(),
                          {'count': 1, 'next': None, 'previous': None,
                           'results': [
                               {'id': self.module.pk,
                                'numbers': None,
                                'title': 'test',
                                'description': None,
                                'owner': self.user.pk}
                           ]})

    def test_create_module(self):
        """Тестирование создания модуля"""
        data = {"title": 'test2', 'description': 'description_exampl'}
        response = self.client.post(reverse('educational_modules:module_create'), data=data)

        # Проверяем статус вывода списка
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED)

        #  Проверка корректности данных
        self.assertEquals(Module.objects.all().count(), 2)

        # Проверка подстановки по умолчанию текущего пользователя
        self.assertEquals(response.json().get("owner"), self.user.pk)

    def test_retrieve_module(self):
        """Тестирование вывода данных по отдельному модуля"""
        response = self.client.get(reverse('educational_modules:module_retrieve', args=[self.module.pk]))

        # Проверка статус вывода списка
        self.assertEquals(response.status_code,
                          status.HTTP_200_OK)

        #  Проверка корректности данных
        self.assertEquals(response.json(),
                          {'id': self.module.pk,
                           'numbers': None,
                           'title': 'test',
                           'description': None,
                           'owner': self.user.pk})

    def test_update_module(self):
        """Тестирование обновления модуля"""
        data = {"title": 'test3'}
        response = self.client.patch(reverse('educational_modules:module_update', args=[self.module.pk]), data=data)

        # Проверяем статус вывода списка
        self.assertEquals(response.status_code,
                          status.HTTP_200_OK)

        # Проверка изменения
        self.assertEquals(response.json().get("title"), "test3")

    def test_delete_module(self):
        """Тестирование удаления модуля"""

        response = self.client.delete(reverse('educational_modules:module_delete', args=[self.module.pk]))

        # Проверяем статус вывода списка
        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT)

        #  Проверка корректности данных
        self.assertEquals(Module.objects.all().count(), 0)
