from django.shortcuts import render
from .models import Restaurant
import csv

def restaurant_list(request):
    if not Restaurant.objects.exists():
        with open('csvfile/restaurants.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Restaurant.objects.create(**row)

    restaurants = Restaurant.objects.filter(has_table_booking=True, has_online_delivery=True).order_by('-aggregate_rating')
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants})
