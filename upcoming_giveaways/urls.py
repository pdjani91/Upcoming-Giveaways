from django.contrib import admin
from django.urls import path,include
from upcoming_giveaways.core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',views.home, name='home'),
	path('signup/',views.signup, name='signup'),
	path('books/',views.book_list,name='book_list'),
    path('books/upload/',views.upload_book,name='upload_book'),
    path('books/<int:pk>/',views.delete_book,name='delete_book'),
	path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)