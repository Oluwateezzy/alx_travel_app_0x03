from rest_framework.decorators import api_view
from rest_framework.response import Response

from listings.tasks import send_booking_confirmation_email


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "message": "Welcome to ALX Travel App API",
        }
    )


class BookingViewSet(viewsets.ModelViewSet):
    # ... your existing code ...

    def perform_create(self, serializer):
        booking = serializer.save(user=self.request.user)
        # Trigger the email task asynchronously
        send_booking_confirmation_email.delay(booking.id)
        return booking
