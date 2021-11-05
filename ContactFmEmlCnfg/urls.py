from django.contrib import admin
from django.urls import path

from home.views import contact

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Used in production
