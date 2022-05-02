
from django.contrib import admin
from django.urls import path, include
from usr_auth import views as v_u
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',v_u.register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('', include('main.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
