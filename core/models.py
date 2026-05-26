from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model for MyBook.
    Extends Django's built-in AbstractUser and adds a role field.
    """

    # Role choices — these are the only valid values for the role field
    TEACHER = 'teacher'
    STUDENT = 'student'

    ROLE_CHOICES = [
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=STUDENT,     # default role is student
    )

    profile_picture = models.ImageField(
        upload_to='profiles/',   # saves to media/profiles/
        null=True,
        blank=True,
    )

    def is_teacher(self):
        """Helper method — use in views and templates"""
        return self.role == self.TEACHER

    def is_student(self):
        """Helper method — use in views and templates"""
        return self.role == self.STUDENT

    def __str__(self):
        return f"{self.get_full_name()} ({self.role})"