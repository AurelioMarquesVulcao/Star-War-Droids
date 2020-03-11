from rest_framework import serializers
from .models import Demanda


class DemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = ['id', 'nome', 'descricao', 'rua_entrega', 'complemento', 'cep', 'estado', 'cidade', 'tel_contato', 'user', 'status']