from django.urls import path
from . import views
from django.core.cache import cache
from .models import Property

urlpatterns = [
    path("properties/", views.property_list, name="property_list"),
]

def get_all_properties():
    # Try to get from Redis cache
    properties = cache.get("all_properties")
    if not properties:
        # If not in cache, fetch from database
        properties = list(Property.objects.all().values(
            "id", "title", "description", "price", "location", "created_at"
        ))
        # Store in Redis for 1 hour (3600 seconds)
        cache.set("all_properties", properties, 3600)
    return properties