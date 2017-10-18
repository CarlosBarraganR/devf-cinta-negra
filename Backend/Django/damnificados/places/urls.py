from django.conf.urls import url
from .views import PlacesApi, PlaceApi # PersonaHasLugaresApi #Importar la view

urlpatterns = [
    url(r'^$', PlacesApi.as_view(), name = "places_endpoint"),
    url(r'(?P<pk>[0-9]+)/$', PlaceApi.as_view(), name = 'place_endpoint')
    # url(r'/personaHasLugares', PersonaHasLugaresApi.as_view())
]