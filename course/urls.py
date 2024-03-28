from django.urls import path
from course import views

urlpatterns = [
    path("", views.CourseListAPIView.as_view()),
    path("top/", views.TopCourseListAPIView.as_view()),
    path("<int:pk>/", views.CourseRetriveAPIView.as_view()),
    path("lesson/<int:pk>/", views.LessonRetrieveAPIView.as_view()),
    path("feedback/", views.FeedbackCreateAPIView.as_view()),
]
