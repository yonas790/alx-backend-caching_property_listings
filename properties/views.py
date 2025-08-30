from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property

# Cache the view for 15 minutes (60*15 seconds)
@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values("id", "title", "description", "price", "location", "created_at")
    return JsonResponse(list(properties), safe=False)
