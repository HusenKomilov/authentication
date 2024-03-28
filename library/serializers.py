from rest_framework import serializers
from . import models


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = (
            'id',
            'title',
            'image',
            'author',
            'rating',
            'created_at',
            'updated_at',
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ( 
                'id',
                'title',
                'author',
                'price',
                'level',
                'category',
                'language',
                'number_of_pages',
                'published_at',
                'is_discount',
                'is_saved',
                'image',
                'description',
                'rating',
                'created_at',
                'updated_at',
                )
    

class LibararySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = [
            'id',
            'title',
            'price',
            'rating',
            'language',
            'level',
            'category',
            'author',
            'is_saved',
            'image',
            'created_at',
            'updated_at',
        ]

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = (
            'id',
            'title',
            'price',
            'level',
            'author',
            'number_of_pages',
            'published_at',
            'is_saved',
            'description',
            'image',
            'created_at',
            'updated_at',
        )
