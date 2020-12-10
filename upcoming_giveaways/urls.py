from django.contrib import admin
from django.urls import path,include
from upcoming_giveaways.core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',views.home, name='home'),
	path('signup/',views.signup, name='signup'),
	path('secret/',views.secret_page,name='secret'),
	path('secret2/', views.SecretPage.as_view(),name='secret2'),
	path('upload/', views.upload, name='upload'),
	path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)