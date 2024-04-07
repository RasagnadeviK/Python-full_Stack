from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
    path('about/',include('pages.urls')),
path('accounts/', include('allauth.urls')),
path('oauth/', include('social_django.urls', namespace='social')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
