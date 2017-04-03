from django.db import models

class Department(models.Model):
    """Department model."""

    name = models.CharField(max_length=50, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""

        return "{}".format(self.name)

class Employee(models.Model):
    """Employee model."""

    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""

        return "{}".format(self.name)
