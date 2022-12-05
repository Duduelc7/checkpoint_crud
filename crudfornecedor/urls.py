"""crudfornecedor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crud_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Empresas', views.EmpresaserializerViewSet, basename= 'Empresas')
router.register('MatrizContaFornecedor', views.MatrizContaFornecedorViewSet, basename= 'MatrizContaFornecedor')
router.register('Projetos', views.ProjetosViewSet, basename= 'Projetos')
router.register('Dimcontas', views.DimcontasViewSet, basename= 'Dimcontas')




urlpatterns = [
    path('index/',views.IndexView.as_view(),name='index'),
    path('admin/',admin.site.urls,name='admin'),
    path('app/',include('crud_app.urls',namespace='crud_app')),
    path('', include('usuarios.urls')),
    path('api/',include(router.urls))
]
