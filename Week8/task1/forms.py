from django import forms
from .models import Restaurant, Dish, Review

class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ["name", "phone", "city", "user"]

class DishForm(forms.ModelForm):
	class Meta:
		model = Dish
		fields = ["name", "description", "price", "user", "restaurant"]

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ["comment", "rating", "date"]