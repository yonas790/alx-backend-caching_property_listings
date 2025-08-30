from django.core.cache import cache
from .models import Property

def getallproperties():
    # Try to get from Redis cache using the exact key "allproperties"
    properties = cache.get("allproperties")
    if not properties:
        properties = list(Property.objects.all().values(
            "id", "title", "description", "price", "location", "created_at"
        ))
        cache.set("allproperties", properties, 3600)  # 1 hour
    return properties
