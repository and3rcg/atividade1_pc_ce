from rest_framework.response import Response
from rest_framework import status, viewsets

from api.serializers import ArmaSerializer, CalibreSerializer, MunicaoSerializer, ObjetoSerializer, ObjetoTipoSerializer
from .models import Calibre, ObjetoTipo, Objeto, Arma, Municao


class ObjetoViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer


class CalibreViewset(viewsets.ModelViewSet):
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer


class ObjetoTipoViewset(viewsets.ModelViewSet):
    queryset = ObjetoTipo.objects.all()
    serializer_class = ObjetoTipoSerializer


class ArmaViewset(viewsets.ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

    def create(self, request):
        arma = ObjetoTipo.objects.get(tipo_de_objeto='arma')
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            objeto = Objeto.objects.create(objeto_tipo=arma)
            nova_arma = Arma.objects.create(id=objeto, **serializer.validated_data)
            return Response(data=ArmaSerializer(nova_arma).data, status=status.HTTP_201_CREATED)

        return Response(data={'erro': 'Valores inválidos.'}, status=status.HTTP_400_BAD_REQUEST)


class MunicaoViewset(viewsets.ModelViewSet):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer

    def create(self, request):
        municao = ObjetoTipo.objects.get(tipo_de_objeto='munição')
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            objeto = Objeto.objects.create(objeto_tipo=municao)
            nova_municao = Municao.objects.create(id=objeto, **serializer.validated_data)
            return Response(data=MunicaoSerializer(nova_municao).data, status=status.HTTP_201_CREATED)

        return Response(data={'erro': 'Valores inválidos.'}, status=status.HTTP_400_BAD_REQUEST)
