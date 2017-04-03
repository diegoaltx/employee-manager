from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Department, Employee

class DepartmentModelTestCase(TestCase):
    """Test suite for the Department model."""

    def test_model_can_create_an_department(self):
        old_count = Employee.objects.count()

        department = Department(name="Department 1")
        department.save()

        new_count = Department.objects.count()

        self.assertNotEqual(old_count, new_count)

class EmployeeModelTestCase(TestCase):
    """Test suite for the Employee model."""

    def test_model_can_create_an_employee(self):
        old_count = Employee.objects.count()

        department = Department(name="Department 2")
        department.save()

        employee = Employee(
            name='Employee One',
            email='employee.one@testcompany.com',
            department=department
        )
        employee.save()

        new_count = Employee.objects.count()

        self.assertNotEqual(old_count, new_count)

class DepartmentAPITestCase(TestCase):
    """Test suite for the Departments and DepartmentDetail views."""

    def setUp(self):
        """Defines the test client and other test params."""

        client = APIClient()

        api_user = User.objects.create_user(
            username='apiuser_department',
            email="apiuser_department@testcompany.com",
            password="q1w2e3r4"
        )

        client.force_authenticate(user=api_user)

        self.client = client

    def test_api_can_create_an_department(self):
        """Test if api has department creation capability."""

        department_data = {'name': 'Department One'}

        response = self.client.post(
            reverse('departments'),
            department_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_an_department(self):
        """Test if api can get a given department."""

        department = Department(name='Department Two')
        department.save()

        response = self.client.get(
            reverse('department_details', kwargs={'pk': department.id}),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, department)

    def test_api_can_update_department(self):
        """Test if api can update a given department."""

        department = Department(name='Department Three')
        department.save()

        new_data = {'name': 'Department Updated'}

        response = self.client.patch(
            reverse('department_details', kwargs={'pk': department.id}),
            new_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_department(self):
        """Test if api can delete a department."""

        department = Department(name='Department Four')
        department.save()

        response = self.client.delete(
            reverse('department_details', kwargs={'pk': department.id}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class EmployeeAPITestCase(TestCase):
    """Test suite for the Employees and EmployeeDetail views."""

    def setUp(self):
        """Defines the test client and other test params."""

        client = APIClient()

        api_user = User.objects.create_user(
            username='apiuser_employee',
            email="apiuser_employee@testcompany.com",
            password="q1w2e3r4"
        )

        client.force_authenticate(user=api_user)

        self.client = client

        department = Department(name='Test Department')
        department.save()

        self.department = department

    def test_api_can_create_an_employee(self):
        """Test if api has employee creation capability."""

        employee_data = {
            'name': 'Person One',
            'email': 'person.one@testcompany.com',
            'department_id': self.department.id
        }

        response = self.client.post(
            reverse('employees'),
            employee_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_an_employee(self):
        """Test if api can get a given employee."""

        employee = Employee(
            name='Person Two',
            email='person.two@testcompany.com',
            department=self.department
        )
        employee.save()

        response = self.client.get(
            reverse('employee_details', kwargs={'pk': employee.id}),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, employee)

    def test_api_can_update_employee(self):
        """Test if api can update a given employee."""

        employee = Employee(
            name='Person Three',
            email='person.three@testcompany.com',
            department=self.department
        )
        employee.save()

        new_data = {'name': 'Person Updated'}

        response = self.client.patch(
            reverse('employee_details', kwargs={'pk': employee.id}),
            new_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_employee(self):
        """Test if api can delete an employee."""

        employee = Employee(
            name='Person Four',
            email='person.four@testcompany.com',
            department=self.department
        )
        employee.save()

        response = self.client.delete(
            reverse('employee_details', kwargs={'pk': employee.id}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
