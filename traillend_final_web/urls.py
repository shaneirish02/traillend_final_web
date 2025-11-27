from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from core.views import apply_migrations
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

urlpatterns = [
    path("apply-migrations/", apply_migrations),
    path("static-test/<path:path>", never_cache(serve))
    path("admin/", admin.site.urls),
    path("", lambda request: redirect("login")),  # redirect root to login page
    path("", include('core.urls')),
]

