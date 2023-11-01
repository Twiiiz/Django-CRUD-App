from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

def year_validation(year):
    current_year = datetime.now().year
    if year < 0 or year > current_year:
        raise ValidationError(f"Year must be between 0 and {current_year}")

# Create your models here.
class Book(models.Model):
  name = models.CharField(max_length=40)
  author = models.CharField(max_length=55)
  genre = models.CharField(max_length=55)
  publisher = models.CharField(max_length=30)
  release_year = models.IntegerField(validators=[year_validation])

  class Meta:
    db_table ='book'