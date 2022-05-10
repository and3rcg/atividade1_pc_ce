# importar os viewsets
from api.views import ArmaViewset, CalibreViewset, MunicaoViewset, ObjetoViewset, ObjetoTipoViewset
from rest_framework import routers

api_router = routers.DefaultRouter()

# registrar os viewsets
api_router.register('armas', ArmaViewset)
api_router.register('calibres', CalibreViewset)
api_router.register('municoes', MunicaoViewset)
api_router.register('objetos', ObjetoViewset)
api_router.register('tipos_objetos', ObjetoTipoViewset)
