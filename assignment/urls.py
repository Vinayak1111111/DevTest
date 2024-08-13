from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('data_processor.urls')),  # Includes the app's URLs under the '/upload/' path
]
