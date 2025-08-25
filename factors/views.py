from rest_framework.generics import CreateAPIView,ListAPIView
from .models import Activity
from .serializers import ActivityCreateSerializer
from rest_framework.permissions import IsAuthenticated

class ActivityCreateAPIView(CreateAPIView):
    serializer_class = ActivityCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GetMyActivity(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivityCreateSerializer
    permission_classes = [IsAuthenticated]