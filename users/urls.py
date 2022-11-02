from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'
urlpatterns = [
    path('profile/<username>', views.show_profile, name='profile'),
    path('edit', views.edit_profile, name='edit_profile'),
    path('json', views.show_json, name='show_json'),
    path('saldo', views.edit_saldo, name='edit_saldo'),
    path('topup', views.show_topup, name='show_topup')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
