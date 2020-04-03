from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as UserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', UserView.UserLoginView.as_view(), name='login'),
    path('logout/', UserView.UserLogoutView.as_view(), name='logout'),
    path('register/', UserView.Register,name='register'),
    path('profile/', UserView.UserProfile,name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
