
from django.urls import include,path
from etl.views import *

urlpatterns = [
    path('',CargaDatos.as_view(),name="carga_menu"),
    path('cargabd',EtlBD.as_view(),name="etl_bd"),
    path('cargaretorno',CargaRetorno.as_view(),name='etl_retorno')
    

]
