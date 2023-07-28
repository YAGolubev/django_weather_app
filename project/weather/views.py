import requests
from decouple import config
from django.shortcuts import render

from .models import City


def index(request):
    url = (
        'https://api.openweathermap.org/data/2.5/weather'
        '?q={}&units=metric&lang=ru&appid=' + config('OPENWEATHER_APPID')
    )

    all_cities = []
    cities = City.objects.all()[:3]
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': round(res['main']['temp'], 1),
            'description': res['weather'][0]['description'],
            'icon': res['weather'][0]['icon'],
        }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'alert_variant': [
            'primary',
            'secondary',
            'success',
            'danger',
            'warning',
            'info',
            'light',
            'dark',
        ],
    }
    return render(request, 'weather/index.html', context)
