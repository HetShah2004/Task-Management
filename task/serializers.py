from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_by']

    def validate(self, data):
        user = self.context['request'].user

        if 'assigned_to' in data:
            if user.role not in ['admin', 'manager']:
                raise serializers.ValidationError("Only admin and manager can assign tasks.")
            
        if 'due_date' in data:
            from django.utils import timezone
            if data['due_date'] < timezone.now().date():
                raise serializers.ValidationError("Due date cannot be in the past.")
            
        return data

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.role == 'user':
            allowed_fields = ['status']
            for field in validated_data:
                if field not in allowed_fields:
                    raise serializers.ValidationError(f"Users can only update the following fields: {', '.join(allowed_fields)}")
        
        return super().update(instance, validated_data)