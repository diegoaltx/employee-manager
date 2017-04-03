from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Employee

class ModelTestCase(TestCase):
    """Test suite for the Employee model."""

    def setUp(self):
        pass

    def test_model_can_create_an_employee(self):
        old_count = Employee.objects.count()

        employee = Employee(
            name='Diego Teixeira',
            email='diegoteixeir4@gmail.com',
            department='IT'
        )
        employee.save()

        new_count = Employee.objects.count()

        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test params."""
        self.client = APIClient()

    def test_api_can_create_an_employee(self):
        """Test if api has employee creation capability."""
        employee_data = {
            'name': 'Person One',
            'email': 'person.one@testcompany.com',
            'department': 'IT'
        }

        response = self.client.post(
            reverse('create'),
            employee_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_an_employee(self):
        """Test if api can get a given employee."""
        employee = Employee(
            name='Person Two',
            email='person.two@testcompany.com',
            department='Marketing'
        )
        employee.save()

        response = self.client.get(
            reverse('details', kwargs={'pk': employee.id}),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, employee)

    def test_api_can_update_employee(self):
        """Test if api can update a given employee."""
        employee = Employee(
            name='Person Two',
            email='person.three@testcompany.com',
            department='Sales'
        )
        employee.save()

        new_data = {'name': 'Person Updated'}

        response = self.client.patch(
            reverse('details', kwargs={'pk': employee.id}),
            new_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_employee(self):
        """Test if api can delete an employee."""
        employee = Employee(
            name='Person Four',
            email='person.four@testcompany.com',
            department='RH'
        )
        employee.save()

        response = self.client.delete(
            reverse('details', kwargs={'pk': employee.id}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
