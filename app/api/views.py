from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import get_object_or_404
from .models import Goal
from .serializers import GoalSerializer


# Create your views here.

class GoalView(ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

    def perform_create(self, serializer):
        goal = get_object_or_404(Goal, id=self.request.data.get('aligned_to'))
        return serializer.save(goal=goal)


class SingleGoalView(RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
