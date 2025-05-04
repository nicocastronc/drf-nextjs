
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .views import TestView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TestView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
