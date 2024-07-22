from django.contrib import admin
from django.urls import path
from sitio_usuarios.carga.views import upload_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_csv, name='upload_csv'),
]
