from django.conf.urls import url
from .views import PlacesApi#, PersonaHasLugaresApi #Importar la view

urlpatterns = [
    url(r'^$', PlacesApi.as_view()),
    # url(r'/personaHasLugares', PersonaHasLugaresApi.as_view())
]