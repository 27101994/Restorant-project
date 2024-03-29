# Generated by Django 4.2.11 on 2024-03-09 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_location_alter_restaurant_cuisines_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='online_delivery',
            new_name='is_delivering_now',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='table_booking',
            new_name='switch_to_order_menu',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='location',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='name',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='rating',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='aggregate_rating',
            field=models.FloatField(default=4.5),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='average_cost_for_two',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='currency',
            field=models.CharField(blank=True, default='USD', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='has_online_delivery',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='has_table_booking',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='locality',
            field=models.CharField(default='Sample Locality', max_length=255),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='locality_verbose',
            field=models.CharField(default='Verbose Locality', max_length=255),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='price_range',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rating_color',
            field=models.CharField(default='Green', max_length=20),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rating_text',
            field=models.CharField(default='Excellent', max_length=20),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='votes',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='cuisines',
            field=models.CharField(default='Italian, Chinese', max_length=255),
        ),
    ]
