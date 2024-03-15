from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ledger.urls', namespace='ledger')),
    path('accounts/', include('django.contrib.auth.urls')),
]