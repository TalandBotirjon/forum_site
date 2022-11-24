
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Forum site.",
        description="Savol javob saytini qilish.",
        default_version="v1",
        terms_of_service=0,
        contact=openapi.Contact(email="ergashovbotirjon4@gmail.com", link="https://github.com/TalandBotirjon/"),
        license=openapi.License(name="Savol javob sayti."),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("forum.urls")),
    path("api/auth/", include("rest_framework.urls")),
    path("api/swagger/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger"),
]
