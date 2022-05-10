from rest_framework.serializers import ModelSerializer
from .models import Arma, Calibre, Municao, Objeto, ObjetoTipo


class CalibreSerializer(ModelSerializer):
    class Meta:
        model = Calibre
        fields = '__all__'


class ObjetoTipoSerializer(ModelSerializer):
    class Meta:
        model = ObjetoTipo
        fields = '__all__'


class ArmaSerializer(ModelSerializer):
    class Meta:
        model = Arma
        fields = '__all__'
        read_only_fields = ['id']


class MunicaoSerializer(ModelSerializer):
    class Meta:
        model = Municao
        fields = '__all__'
        read_only_fields = ['id']


class ObjetoSerializer(ModelSerializer):
    class Meta:
        model = Objeto
        fields = '__all__'
