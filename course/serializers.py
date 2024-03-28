from rest_framework import serializers
from django.contrib.auth.models import User
from course import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            "id",
            "title",
        )


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Level
        fields = (
            "id",
            "title",
        )


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = (
            "id",
            "title",
        )


class LessonUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = models.LessonUser
        fields = ("id", "lesson", "user", "watching_at", "is_complete")


class LessonSerializer(serializers.ModelSerializer):
    lesson_users = LessonUserSerializer(many=True)

    class Meta:
        model = models.Lesson
        fields = (
            "id",
            "title",
            "content",
            "banner",
            "video",
            "video_duration",
            "unit",
            "lesson_users",
            "created_at",
            "updated_at",
        )


class LessonRetriveSerializer(serializers.ModelSerializer):
    lesson_users = LessonUserSerializer(many=True)

    # prev = LessonSerializer()
    # next = LessonSerializer()

    class Meta:
        model = models.Lesson
        fields = (
            "id",
            "title",
            "content",
            "banner",
            "video",
            "video_duration",
            "unit",
            # "prev",
            # "next",
            "lesson_users",
            "created_at",
            "updated_at",
        )

    # def to_representation(self, instance):
    #     lessons = list(
    #         Lesson.objects.all().filter(unit=instance.unit).order_by("-created_at")
    #     )

    #     json = super().to_representation(instance)
    #     prev = ""
    #     next = ""

    #     if lessons.index(instance) != 0:
    #         prev = lessons[lessons.index(instance) - 1]

    #     if lessons.index(instance) != len(lessons) - 1:
    #         next = lessons[lessons.index(instance) + 1]

    #     json.prev = prev
    #     json.next = next

    #     return json


class UnitSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = models.Unit
        fields = ("id", "title", "course", "lessons")


class FeedBackSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = models.FeedBack
        fields = (
            "id",
            "user",
            "course",
            "stars",
            "content",
            "created_at",
            "updated_at",
        )


class CourseUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = models.CourseUser
        fields = (
            "id",
            "course",
            "user",
            "is_complete",
            "is_favorite",
            "created_at",
            "updated_at",
        )


class CourseSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    level = LevelSerializer()
    category = CategorySerializer()
    units = UnitSerializer(many=True)

    class Meta:
        model = models.Course
        fields = (
            "id",
            "title",
            "price",
            "author",
            "language",
            "level",
            "category",
            "rating",
            "units",
            "created_at",
            "updated_at",
        )


class CourseSingleSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    level = LevelSerializer()
    category = CategorySerializer()
    units = UnitSerializer(many=True)
    feedbacks = FeedBackSerializer(many=True)
    course_users = CourseUserSerializer(many=True)

    class Meta:
        model = models.Course
        fields = (
            "id",
            "title",
            "price",
            "author",
            "language",
            "level",
            "category",
            "rating",
            "feedbacks",
            "units",
            "course_users",
            "created_at",
            "updated_at",
        )


class ReportSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)
    feedback = FeedBackSerializer()

    class Meta:
        model = models.Report
        fields = ("id", "subject", "content", "user", "feedback")
