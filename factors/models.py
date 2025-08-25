from django.db import models
from django.conf import settings

class Activity(models.Model):
    CATEGORY_CHOICES = [
        ('transport', 'Transport'),
        ('energy', 'Energy'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    co2_emission = models.FloatField(help_text="CO₂ in kg")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.co2_emission}kg"

    @staticmethod
    def get_total_co2(user):
        from django.db.models import Sum
        total = Activity.objects.filter(user=user).aggregate(
            all_co2=Sum("co2_emission")
        )["all_co2"] or 0
        return total

    class Meta:
        db_table = "factors_activity"

