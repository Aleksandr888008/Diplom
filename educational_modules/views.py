from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from educational_modules.models import Module
from educational_modules.paginators import ListPaginator
from educational_modules.permissions import IsOwner
from educational_modules.serializers import ModulSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    """Создание модуля"""
    serializer_class = ModulSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Автоматическое сохранение владельца при создании нового объекта"""
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class ModuleListAPIView(generics.ListAPIView):
    """Просмотр своих модулей"""
    queryset = Module.objects.all()
    serializer_class = ModulSerializer
    permission_classes = [IsAuthenticated | IsOwner]
    pagination_class = ListPaginator

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """Детальный просмотр модуля"""
    queryset = Module.objects.all()
    serializer_class = ModulSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """Изменение модуля"""
    queryset = Module.objects.all()
    serializer_class = ModulSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """Удаление модуля"""
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
