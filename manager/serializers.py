from rest_framework import serializers
from .models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Department
        fields = ('id', 'name')

class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance."""

    department = DepartmentSerializer(read_only=True)
    department_id = serializers.IntegerField()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Employee
        fields = (
            'id', 'name', 'email', 'department_id', 'department',
            'date_created', 'date_modified'
        )
        read_only_fields = ('date_created', 'date_modified')
