from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Goal
from .serializers import GoalSerializer


# Create your views here.

class GoalView(ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class SingleGoalView(RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
