from django.db import models

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(
        Project,
        related_name="employees"
    )

    def __str__(self):
        return self.name
