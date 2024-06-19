from django.urls import path, include, re_path  # Import include function

# Other imports as needed
from django.contrib import admin
from cms_project.swagger import schema_view
from django.views.generic import RedirectView

# Define your urlpatterns
urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/", include("cms_app.urls")
    ),  # Include your app's URLs using include function
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # Redirect root URL to Swagger UI
    re_path(r"^$", RedirectView.as_view(url="/swagger/")),
]
