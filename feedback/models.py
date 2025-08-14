from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

from django.db import models

class Feedback(models.Model):
    RATING_CHOICES = [
        (1, '⭐ 1'),
        (2, '⭐ 2'),
        (3, '⭐ 3'),
        (4, '⭐ 4'),
        (5, '⭐ 5'),
    ]

    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"
