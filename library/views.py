from .serializers import BookSerializer, RecommendationSerializer, LibararySerializer, \
    BookDetailSerializer
from .models import Book
from rest_framework import generics
import django_filters

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RecommendationAPIView(generics.ListAPIView):
    queryset = Book.objects.all().order_by('-rating')
    serializer_class = RecommendationSerializer


class LibraryAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = LibararySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['language', 'level', 'category', 'rating',]


class BookDetailAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer




    
