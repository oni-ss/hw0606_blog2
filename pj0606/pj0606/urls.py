from django.contrib import admin
from django.urls import path, include
import blogapp.views
import blogapp.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blogapp/', include(blogapp.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
