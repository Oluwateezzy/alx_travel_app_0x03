from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_booking_confirmation_email(booking_id):
    from listings.models import Booking  # Import here to avoid circular imports

    try:
        booking = Booking.objects.get(id=booking_id)
        subject = f"Booking Confirmation - {booking.listing.title}"
        message = f"""
        Thank you for your booking!
        
        Booking Details:
        - Listing: {booking.listing.title}
        - Check-in: {booking.check_in}
        - Check-out: {booking.check_out}
        - Total Price: ${booking.total_price}
        
        We look forward to hosting you!
        """
        recipient_list = [booking.user.email]
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )
        return f"Email sent to {booking.user.email}"
    except Booking.DoesNotExist:
        return "Booking not found"
