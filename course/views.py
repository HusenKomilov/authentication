from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from course import serializers
from course import models


class CourseListAPIView(ListAPIView):
    queryset = models.Course.objects.all().order_by("-created_at")
    serializer_class = serializers.CourseSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    filterset_fields = ("category", "level", "language", "rating")
    search_fields = [
        "title",
    ]


class CourseRetriveAPIView(RetrieveAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSingleSerializer


class TopCourseListAPIView(ListAPIView):
    queryset = models.Course.objects.all().order_by("-rating")[:4]
    serializer_class = serializers.CourseSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonRetriveSerializer


class FeedbackCreateAPIView(CreateAPIView):
    queryset = models.FeedBack.objects.all()
    serializer_class = serializers.FeedBackSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.user = user
        serializer.save()
        return serializer
