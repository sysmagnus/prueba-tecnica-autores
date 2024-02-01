from django.urls import path
from .views import AutorListCreateView, AutorDetailView, LibroListCreateView, LibroDetailView

urlpatterns = [
    path('authors/', AutorListCreateView.as_view()),
    path('authors/<int:pk>/', AutorDetailView.as_view()),
    path('books/', LibroListCreateView.as_view()),
    path('books/<int:pk>/', LibroDetailView.as_view()),
]
