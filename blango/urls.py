from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import blog.views
import blango_auth.views
from blango_auth.forms import BlangoRegistrationForm
from django_registration.backends.activation.views import RegistrationView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", blog.views.index, name="index"),
    path("post/<slug:slug>/", blog.views.post_detail, name="post-detail"),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=BlangoRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
    path("accounts/", include("allauth.urls")),
    path("api/v1/", include("blog.api.urls")),
    path("post-table/", blog.views.post_table, name="blog-post-table"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)