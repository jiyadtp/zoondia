from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.login,name='login'),
    path('login-check',views.login_check,name="login-check"),
    path('register',views.register,name='register'),
    path('register-data', views.register_data, name='register-data'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('create-url',views.create_url,name='create-url'),
    path('edit-url',views.edit_url,name='edit-url'),
    path('delete-url/<int:id>',views.delete_url,name='delete-url'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)