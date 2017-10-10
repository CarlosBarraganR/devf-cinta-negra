from django.conf.urls import url
from .views import PlacesApi #Importar la view

urlpatterns = [
    url(r'^$', PlacesApi.as_view())
]