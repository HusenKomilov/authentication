from django.urls import path
from news import views

urlpatterns = [
    path('news/', views.MainListAPIView.as_view()),
    path('news/<int:pk>/', views.NewsRetrieveAPIView.as_view()),
    path('rules/', views.RulesAPIView.as_view()),
]
