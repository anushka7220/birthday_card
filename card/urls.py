from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from .views import cupcake_preview

app_name = 'card'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='card:create_card', permanent=False)),  # Add this line
    path('create/', views.create_card, name='create_card'),
    path('preview/<int:card_id>/', views.preview_card, name='preview_card'),
    path('preview/', cupcake_preview, name='cupcake_preview'),
]