from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from account.views import home

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^question/', include('question.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^account/', include('userprofile.urls')),
    url(r'^notification/', include('notification.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
