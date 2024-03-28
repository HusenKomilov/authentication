from django.contrib import admin
from course import models


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

    class Meta:
        abstract = True





@admin.register(models.Category)
class CategoryAdmin(BaseAdmin):
    pass


@admin.register(models.Level)
class LevelAdmin(BaseAdmin):
    pass


@admin.register(models.Language)
class LanguageAdmin(BaseAdmin):
    pass


@admin.register(models.Course)
class CourseAdmin(BaseAdmin):
    readonly_fields = ("rating", "created_at", "updated_at")


@admin.register(models.CourseUser)
class CourseUserAdmin(BaseAdmin):
    pass


@admin.register(models.Unit)
class UnitAdmin(BaseAdmin):
    pass


@admin.register(models.Lesson)
class LessonAdmin(BaseAdmin):
    pass


@admin.register(models.LessonUser)
class LessonUserAdmin(BaseAdmin):
    pass


@admin.register(models.FeedBack)
class FeedBackAdmin(BaseAdmin):
    pass


@admin.register(models.Report)
class ReportAdmin(BaseAdmin):
    pass
