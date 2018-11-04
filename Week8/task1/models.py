from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	#telephone = models.CharField(max_length=11)
	city = models.CharField(max_length=255)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Dish(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=500)
	price = models.IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')

	def __str__(self):
		return self.name

class Review(models.Model):
	comment = models.CharField(max_length=500)
	rating = models.IntegerField()
	date = models.DateField()

	def __str__(self):
		return self.comment

class RestReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='rest_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.restaurant)
