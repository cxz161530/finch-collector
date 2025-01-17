from django.db import models
from django.urls import reverse

MEALS = (
    ('B','Breakfast'),
    ('L','Lunch'),
    ('D', 'Dinner')
)

class Finch(models.Model):
    name=models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        """ make our admin view have name to check obj status in model """
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
              choices=MEALS,
              default=MEALS[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

