from django.shortcuts import render
import requests
from .models import Weather
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.


def get_weather(api_key, location):
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={location}'

    try:
        response = requests.get(url)
        data = response.json()
        weather = {
            'name': data['location']['name'],
            'temperature': data['current']['temperature'],
            'description': data['current']['weather_descriptions'][0],
            'humidity': data['current']['humidity'],
            'pressure': data['current']['pressure'],
            'wind_speed': data['current']['wind_speed'],
            'visibility': data['current']['visibility'],
        }
        return weather, None
    except requests.exceptions.RequestException as e:
        return None, str(e)


def weather(request):
    api_key = '766da02d7d10cef682b2f6bf5412bab5'
    location = request.GET.get('location', 'New York')

    weather_data, error = get_weather(api_key, location)

    if weather_data:
        Weather.objects.create(**weather_data)

    context = {
        'weather_data': weather_data
    }

    return render(request, 'myapp/weather.html', context)


def search_weather(request):
    if request.method == 'GET':
        location = request.GET.get('location')
        if location:
            # Redirect to the weather view with the specified location
            return redirect(reverse('weather') + f'?location={location}')
    return redirect('weather')
