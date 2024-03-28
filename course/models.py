from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Level(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Language(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Course(BaseModel):
    title = models.CharField(max_length=256)
    price = models.IntegerField(default=0)

    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="courses")
    language = models.ForeignKey(
        Language, on_delete=models.PROTECT, related_name="courses"
    )
    level = models.ForeignKey(Level, on_delete=models.PROTECT, related_name="courses")
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="courses"
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.1)],
        editable=False,
        default=0.0,
    )

    def __str__(self):
        return self.title


class CourseUser(BaseModel):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_users"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="course_user")

    is_complete = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.course.title + " " + self.user.full_name


class Unit(BaseModel):
    title = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="units")

    def __str__(self) -> str:
        return self.title


class Lesson(BaseModel):
    title = models.CharField(max_length=256)
    content = models.TextField()

    banner = models.ImageField(upload_to="lessons/banners/")
    video = models.FileField(
        upload_to="lessons/",
        validators=[FileExtensionValidator(allowed_extensions=["mp4"])],
    )

    video_duration = models.PositiveBigIntegerField(default=0)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="lessons")

    def __str__(self) -> str:
        return self.title


class LessonUser(BaseModel):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name="lesson_users"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lesson_user")

    watching_at = models.PositiveBigIntegerField(default=0)

    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.lesson.title + " " + self.user.username


class FeedBack(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="feedbacks"
    )

    stars = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.1)],
    )
    content = models.TextField()

    def __str__(self):
        return self.content


class Report(BaseModel):
    subject = models.CharField(max_length=256)
    content = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    feedback = models.ForeignKey(
        FeedBack, on_delete=models.CASCADE, related_name="reports"
    )

    def __str__(self) -> str:
        return self.subject + " " + self.user.full_name
