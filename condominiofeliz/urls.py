from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pessoas.urls')),
    path('mensagens/', include('mensagens.urls')),
    path('reservas/', include('reservas.urls')),
    path('encomendas/', include('encomendas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

