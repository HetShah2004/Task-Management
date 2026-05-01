from django.db import models
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import IsAdminOrManager

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]

    def get_queryset(self):
        user = self.request.user

        if user.role in ['admin', 'manager']:
            return Task.objects.all()
        
        # Regular users see tasks they created OR tasks assigned to them
        return Task.objects.filter(models.Q(created_by=user) | models.Q(assigned_to=user))
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
