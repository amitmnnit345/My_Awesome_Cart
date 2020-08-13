from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('notes/', include('notes.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)