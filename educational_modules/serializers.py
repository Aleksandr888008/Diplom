from rest_framework import serializers

from educational_modules.models import Module


class ModulSerializer(serializers.ModelSerializer):
    """
    Класс описывающий модель Module. Представляющий какие поля модели будут
    участвовать в процессе сериализации.
    Наследование от базового класса ModelSerializer:
    """
    class Meta:
        model = Module
        fields = '__all__'
