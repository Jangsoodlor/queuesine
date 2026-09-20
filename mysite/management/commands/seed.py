"""Seed the data"""

import csv
import os
from itertools import islice
from django.core.management.base import BaseCommand

from restaurants.models import Restaurant, Menu
from reservations.models import Table, TimeSlot
from datetime import time


class Command(BaseCommand):
    help = "Seeds database with data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            type=str,
            default="data/restaurant_menu_preprocessed_with_images.csv",
            help="Path to the CSV file relative to project root",
        )

        parser.add_argument(
            "--limit",
            type=int,
            default=None,  # None means process all rows by default
            help="Maximum number of rows to process",
        )

    def handle(self, *args, **options):
        file_path = options["file"]
        limit = options["limit"]

        if not os.path.exists(file_path):
            self.stderr.write(self.style.ERROR(f'File "{file_path}" does not exist.'))
            return

        self.stdout.write(self.style.SUCCESS(f"Reading CSV from {file_path}..."))

        self._seed_restaurants(file_path, limit)
        self._seed_menus(file_path, limit)
        self._seed_tables()
        self._seed_available_time()

    def print_seed_success(self, model: str, created_count: int, updated_count: int):
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully inserted {model}!: {created_count}, Updated: {updated_count}"
            )
        )

    def _seed_restaurants(self, file_path: str, limit: int):
        # Track stats
        created_count = 0
        updated_count = 0

        with open(file_path, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = islice(reader, limit) if limit else reader

            for row in rows:
                _, created = Restaurant.objects.update_or_create(
                    name=row["restaurantName"],
                    address=row["restaurantAddress"],
                    defaults={
                        "description": row["restaurantDescription"],
                        "latitude": float(row["restaurantLatitude"]),
                        "longitude": float(row["restaurantLongitude"]),
                        "image": row["restaurantImageUrl"]
                        if row["restaurantImageUrl"]
                        else None,
                        "city": row["market"],
                    },
                )

                if created:
                    created_count += 1
                else:
                    updated_count += 1

        self.print_seed_success(Restaurant.__name__, created_count, updated_count)

    def _seed_menus(self, file_path: str, limit: int):
        created_count = 0
        updated_count = 0

        with open(file_path, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = islice(reader, limit) if limit else reader

            for row in rows:
                restaurant = Restaurant.objects.get(
                    name=row["restaurantName"],
                    address=row["restaurantAddress"]
                    if row["restaurantAddress"]
                    else row["market"],
                )
                if not restaurant:
                    continue
                _, created = Menu.objects.update_or_create(
                    name=row["menuItemName"],
                    description=row["menuItemDescription"],
                    price=float(row["price"]),
                    restaurant=restaurant,
                    category=row["menuItemCategory"],
                    image=row["menuItemImageUrl"] if row["menuItemImageUrl"] else None,
                )
                if created:
                    created_count += 1
                else:
                    updated_count += 1

        self.print_seed_success(Menu.__name__, created_count, updated_count)

    def _seed_tables(self):
        created_count = 0
        updated_count = 0

        restaurants = Restaurant.objects.all()

        # Create default tables for each restaurant
        table_configs = [
            {"name": "Table 1", "capacity": 2},
            {"name": "Table 2", "capacity": 4},
            {"name": "Table 3", "capacity": 6},
            {"name": "Table 4", "capacity": 8},
        ]

        for restaurant in restaurants:
            for config in table_configs:
                _, created = Table.objects.update_or_create(
                    restaurant=restaurant,
                    name=config["name"],
                    defaults={"capacity": config["capacity"]},
                )
                if created:
                    created_count += 1
                else:
                    updated_count += 1

        self.print_seed_success(Table.__name__, created_count, updated_count)

    def _seed_available_time(self):
        created_count = 0
        updated_count = 0

        restaurants = Restaurant.objects.all()

        # Create time slots every 30 minutes from 11:00 to 22:00
        times = [time(hour, minute) for hour in range(11, 23) for minute in [0]]

        for restaurant in restaurants:
            for time_slot in times:
                _, created = TimeSlot.objects.update_or_create(
                    restaurant=restaurant,
                    time_slot=time_slot,
                )
                if created:
                    created_count += 1
                else:
                    updated_count += 1

        self.print_seed_success(TimeSlot.__name__, created_count, updated_count)
