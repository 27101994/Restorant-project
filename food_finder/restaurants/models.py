from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.PositiveIntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=255, default='')
    country_code = models.PositiveIntegerField(default=0)
    city_code = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=255, null=True, blank=True, default='')
    locality = models.CharField(max_length=255, default='')
    locality_verbose = models.CharField(max_length=255, default='')
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    cuisines = models.CharField(max_length=255, default='')
    average_cost_for_two = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=5, null=True, blank=True, default='')
    has_table_booking = models.BooleanField(default=False)
    has_online_delivery = models.BooleanField(default=False)
    is_delivering_now = models.BooleanField(default=False)
    switch_to_order_menu = models.BooleanField(default=False)
    price_range = models.PositiveIntegerField(default=0)
    aggregate_rating = models.FloatField(default=0.0)
    rating_color = models.CharField(max_length=20, default='')
    rating_text = models.CharField(max_length=20, default='')
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
