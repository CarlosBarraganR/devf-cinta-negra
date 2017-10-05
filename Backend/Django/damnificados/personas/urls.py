from django.conf.urls import url
from .views import PersonasApi #Importar la view

urlpatterns = [
    url(r'^$', PersonasApi.as_view())
]