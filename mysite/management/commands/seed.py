"""Seed the data"""

import csv
import os
from itertools import islice
from django.core.management.base import BaseCommand

from restaurants.models import Restaurant, Menu


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
                    description=row["restaurantDescription"],
                    address=row["restaurantAddress"],
                    latitude=float(row["restaurantLatitude"]),
                    longitude=float(row["restaurantLongitude"]),
                    image=row["restaurantImageUrl"]
                    if row["restaurantImageUrl"]
                    else None,
                    city=row["market"],
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
