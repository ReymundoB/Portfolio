
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from briefcase import views
from blog import urls
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name='index'),
    path('blog/', include('blog.urls')  ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
