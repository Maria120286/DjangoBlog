from django import views
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
# from blogproj.users import views as user_views

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

    # user authentications
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('profile/profile_update/', user_views.profile_update, name="profile-update"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
