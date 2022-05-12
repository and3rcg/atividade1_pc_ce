from rest_framework.serializers import ModelSerializer, ValidationError
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

    def validate(self, data):
        if data['quantidade_de_tiros'] <= 0:
            raise ValidationError('A quantidade de tiros não pode ser menor ou igual a zero.')
        elif data['valor_estimado'] <= 0:
            raise ValidationError('O valor estimado não pode ser menor ou igual a zero.')
        return data


class MunicaoSerializer(ModelSerializer):
    class Meta:
        model = Municao
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, data):
        if data['valor_estimado'] <= 0:
            raise ValidationError('O valor estimado não pode ser menor ou igual a zero.')
        return data


class ObjetoSerializer(ModelSerializer):
    class Meta:
        model = Objeto
        fields = '__all__'
