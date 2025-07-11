# ALX Travel App

This is a travel accommodation booking application.

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Seed the database: `python manage.py seed`

## Models

- **Listing**: Represents a property available for booking
- **Booking**: Represents a user's booking of a listing
- **Review**: Represents a user's review of a listing

## API Endpoints

- `/api/listings/`: GET, POST listings
- `/api/listings/<id>/`: GET, PUT, PATCH, DELETE a specific listing
- `/api/bookings/`: GET, POST bookings
- `/api/bookings/<id>/`: GET, PUT, PATCH, DELETE a specific booking