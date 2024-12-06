from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),  # Подключаем URL-ы приложения polls
    path('admin/', admin.site.urls),        # Стандартный путь для админки
]