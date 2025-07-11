from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from listings import views

urlpatterns = [
    # Your API endpoints will go here
]

urlpatterns = format_suffix_patterns(urlpatterns)