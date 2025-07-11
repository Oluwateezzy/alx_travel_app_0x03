from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
import random
from faker import Faker

User = get_user_model()
fake = Faker()


class Command(BaseCommand):
    help = "Seeds the database with sample listings data"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting to seed..."))

        # Create a host user if not exists
        host, created = User.objects.get_or_create(
            username="hostuser",
            defaults={"email": "host@example.com", "password": "testpass123"},
        )

        if created:
            host.set_password("testpass123")
            host.save()

        # Create sample listings
        property_types = ["apartment", "house", "villa", "cabin", "cottage"]
        cities = [
            "New York",
            "Los Angeles",
            "Chicago",
            "Miami",
            "Seattle",
            "Austin",
            "Denver",
        ]

        for i in range(1, 11):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=5),
                address=fake.street_address(),
                city=random.choice(cities),
                country="USA",
                price_per_night=random.randint(50, 500),
                property_type=random.choice(property_types),
                num_bedrooms=random.randint(1, 5),
                num_bathrooms=random.randint(1, 3),
                max_guests=random.randint(2, 10),
                amenities=", ".join(fake.words(nb=5)),
                host=host,
            )
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))

        self.stdout.write(self.style.SUCCESS("Successfully seeded database!"))
