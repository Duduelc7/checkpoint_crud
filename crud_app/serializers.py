from rest_framework import serializers
from crud_app.models import  *

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'
    
class MatrizContaFornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatrizContaFornecedor
        fields = '__all__'

class ProjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = '__all__'

class DimcontasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimcontas
        fields = '__all__'


