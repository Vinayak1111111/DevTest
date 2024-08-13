from django.urls import path
from .views import upload_file

urlpatterns = [
    path('', upload_file, name='upload'),  # Maps the root URL of the app to the upload_file view
]
