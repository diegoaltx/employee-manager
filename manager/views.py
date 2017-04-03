from rest_framework import generics, permissions
from .serializers import DepartmentSerializer, EmployeeSerializer
from .models import Department, Employee

class DepartmentsView(generics.ListCreateAPIView):
    """
    get: Return a list of all existing departments.
    post: Create a new department.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

class DepartmentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Return the given department.
    put: Update the given department.
    patch: Partial update the given department.
    delete: Delete the given department.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

class EmployeesView(generics.ListCreateAPIView):
    """
    get: Return a list of all existing employees.
    post: Create a new employee.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

class EmployeeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Return the given employee.
    put: Update the given employee.
    patch: Partial update the given employee.
    delete: Delete the given employee.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)
