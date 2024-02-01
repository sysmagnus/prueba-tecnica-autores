from django.urls import path
from .views import AutorListCreateView, AutorDetailView, LibroListCreateView, LibroDetailView

urlpatterns = [
    path('autores/', AutorListCreateView.as_view()),
    path('autores/<int:pk>/', AutorDetailView.as_view()),
    path('libros/', LibroListCreateView.as_view()),
    path('libros/<int:pk>/', LibroDetailView.as_view()),
]
