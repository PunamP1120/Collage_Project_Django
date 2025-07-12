from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='list_collages'),
    path('upload/', views.upload_view, name='upload_collage'),
    path('collage/<int:collage_id>/', views.display_view, name='display_collage'),
]
