# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dataupload/', views.data_upload_view, name='dataupload'),
    path('querybuilder/', views.query_builder_view, name='querybuilder'),
    path('users/', views.users_view, name='users'),
]
