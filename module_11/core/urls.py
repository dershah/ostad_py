from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_view
from properties import views as properties_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', accounts_view.register_view, name='register'),
    path('login/', accounts_view.login_view, name='login'),
    path('profile/', accounts_view.profile_view, name='profile'),
    path('profile/edit/', accounts_view.profile_edit_view, name='profile_edit'),
    path('logout/', accounts_view.logout_view, name='logout'),
    path('', properties_view.property_list, name="property_list"),
    path("property/<int:pk>", properties_view.property_detail, name="property_detail"),
    path("property/add/", properties_view.property_create_view, name="property_create"),
    path("property/<int:pk>/edit/", properties_view.property_update_view, name="property_update"),
    path("rentals/", include("rentals.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
