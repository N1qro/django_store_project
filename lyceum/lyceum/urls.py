from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import homepage.views

urlpatterns = [
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("coffee/", homepage.views.joke_index),
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
