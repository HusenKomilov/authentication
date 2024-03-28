from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from news import serializers, models, paginations


# Create your views here.

class MainListAPIView(generics.ListAPIView):
    queryset = models.Post.objects.all().order_by('-created_ad')
    serializer_class = serializers.MainSerializer
    pagination_class = paginations.NewsPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ('title',)


class NewsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.NewsDetailSerializer

    def get_object(self):
        post = models.Post.objects.get(pk=self.kwargs['pk'])
        post.watched += 1
        post.save()
        return post


class RulesAPIView(generics.GenericAPIView):
    queryset = models.Rules.objects.all()
    serializer_class = serializers.RulesSerializers
