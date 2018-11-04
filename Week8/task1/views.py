from django.shortcuts import render, redirect
from .models import Restaurant, Dish, Review, RestReview
from .forms import RestaurantForm, DishForm
from django.contrib.auth.models import User
from django.views import View

# Create your views here.
class home(View):
    def get(self, request):
        rests = Restaurant.objects.all()
        context = {
            'rests': rests,
        }
        return render(request, 'home.html', context)

class rest_list(View):
	def get(self, request, pk):
		rests = Restaurant.objects.all()
		context = {
			'restaurants': rests,
		}
		return render(request, 'rest.html', context)


class add_rest(View):
	def get(self, request):
		form = RestaurantForm()
		context = {
			'form': form,
			'users': User.objects.all(),
		}
		return render(request, 'add_rest.html', context)

	def post(self, request):
		form = RestaurantForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')


class delete_rest(View):
	def get(self, request, pk, fk):
		rest = Restaurant.objects.get(pk=pk)
		rest.delete()
		return redirect('home')


class dish_list(View):
	def get(self, request, pk, fk):
		rest = Restaurant.objects.get(pk=pk)
		dishes = rest.dishes.all()
		reviews = RestReview.objects.filter(restaurant=pk)
		context = {
			'rest': rest,
			'dishes': dishes,
			'reviews': reviews
		}

		return render(request, 'dish.html', context)
