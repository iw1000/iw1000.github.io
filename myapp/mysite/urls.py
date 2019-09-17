from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('news_scraper/', include('news_scraper.urls')),
    path('admin/', admin.site.urls),
]
