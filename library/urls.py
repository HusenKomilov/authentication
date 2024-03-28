from django.urls import path
from .views import BookAPIView, RecommendationAPIView, LibraryAPIView, \
BookDetailAPIView

urlpatterns = [
    path('book/', BookAPIView.as_view()),
    path('recommendation/', RecommendationAPIView.as_view()),
    path('library/', LibraryAPIView.as_view()),
    path('book/detail/', BookDetailAPIView.as_view()),
    ]