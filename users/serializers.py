from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
        Класс описывающий модель User. Представляющий какие поля модели будут
        участвовать в процессе сериализации.
        Наследование от базового класса ModelSerializer:
    """
    class Meta:
        model = User
        fields = '__all__'
