from django.urls import re_path, path
from . import views

app_name = 'file_server0'

urlpatterns = [
    path('download/<str:filename>', views.download),
]


