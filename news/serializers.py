from rest_framework import serializers
from news import models


# class NewsPhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Photo
#         fields = ('photo',)


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id', 'title', 'content', 'main_photo', 'created_ad')


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id', 'title', 'content', 'main_photo', 'created_ad', 'watched',)


class RulesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Rules
        fields = ('description',)
