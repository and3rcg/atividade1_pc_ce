from api.models import Calibre, ObjetoTipo
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Preencher as tabelas calibre e objeto_tipo com os dados iniciais.'

    def handle(self, *args, **kwargs):
        lista_calibres = ['38', '380', '.40', '.45']
        lista_objeto_tipo = ['arma', 'munição']

        for calibre in lista_calibres:
            cal = Calibre(desc_calibre=calibre)
            print(f"Criado objeto '{calibre}' com sucesso!")
            cal.save()

        for objeto_tipo in lista_objeto_tipo:
            obj = ObjetoTipo(tipo_de_objeto=objeto_tipo)
            print(f"Criado objeto '{obj}' com sucesso!")
            obj.save()
