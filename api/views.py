from rest_framework.viewsets import ModelViewSet

from api.serializers import ArmaSerializer, CalibreSerializer, MunicaoSerializer, ObjetoSerializer, ObjetoTipoSerializer
from .models import Calibre, ObjetoTipo, Objeto, Arma, Municao


class ArmaViewset(ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer


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
