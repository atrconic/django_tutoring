from django.urls import path
from .views import CoursesViews, CourseViews, ClassesViews, ClassViews

urlpatterns = [
    path('course/', CoursesViews.as_view()),
    path('course/<int:id>', CourseViews.as_view()),
    path('class/', ClassesViews.as_view()),
    path('class/<int:id>', ClassViews.as_view()),
]



