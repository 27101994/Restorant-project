# Generated by Django 4.2.11 on 2024-03-09 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_rename_online_delivery_restaurant_is_delivering_now_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='id',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='city_code',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='country_code',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='restaurant_id',
            field=models.PositiveIntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='aggregate_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='average_cost_for_two',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='cuisines',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='currency',
            field=models.CharField(blank=True, default='', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='has_online_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='has_table_booking',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='locality',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='locality_verbose',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='price_range',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rating_color',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rating_text',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
