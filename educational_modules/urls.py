from django.urls import path

from educational_modules.apps import EducationalModulesConfig
from educational_modules.views import ModuleCreateAPIView, ModuleListAPIView, ModuleRetrieveAPIView, \
    ModuleUpdateAPIView, ModuleDestroyAPIView

app_name = EducationalModulesConfig.name

urlpatterns = [
    path('module/create/', ModuleCreateAPIView.as_view(), name='module_create'),
    path('module/', ModuleListAPIView.as_view(), name='module_list'),
    path('module/<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module_retrieve'),
    path('module/update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module_update'),
    path('module/delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module_delete'),
]
