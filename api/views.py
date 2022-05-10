from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import ArmaSerializer, CalibreSerializer, MunicaoSerializer, ObjetoSerializer, ObjetoTipoSerializer
from .models import Calibre, ObjetoTipo, Objeto, Arma, Municao


class ArmaViewset(ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

    @action(methods=['post'], detail=True)
    def disparar(self, request, pk=None):
        arma = self.get_object()
        serializer = ArmaSerializer(arma)
        return Response(data=serializer.data, status=status.HTTP_418_IM_A_TEAPOT)


class CalibreViewset(ModelViewSet):
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer


class MunicaoViewset(ModelViewSet):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer


class ObjetoViewset(ModelViewSet):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer


class ObjetoTipoViewset(ModelViewSet):
    queryset = ObjetoTipo.objects.all()
    serializer_class = ObjetoTipoSerializer
