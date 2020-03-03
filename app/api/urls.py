from django.urls import path
from .views import SingleGoalView, GoalView

app_name = 'api'

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('goals/', GoalView.as_view()),
    path('goals/<int:pk>', SingleGoalView.as_view()),
]
