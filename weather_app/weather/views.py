import requests
from django.conf import settings
from django.shortcuts import render
from .models import WeatherData

# def get_weather_data(city):
#     api_key = settings.OPENWEATHERMAP_API_KEY
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     return response.json()

def get_weather_data(city):
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get('cod') == 200:
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],  # Add weather icon
        }
    return None

# def weather_view(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         data = get_weather_data(city)
#         if data.get('cod') == 200:
#             weather_data = {
#                 'city': data['name'],
#                 'temperature': data['main']['temp'],
#                 'description': data['weather'][0]['description'],
#             }
#             # Save to database (optional)
#             WeatherData.objects.create(
#                 city=weather_data['city'],
#                 temperature=weather_data['temperature'],
#                 description=weather_data['description']
#             )
#             return render(request, 'weather/weather.html', {'weather': weather_data})
#         else:
#             error_message = data.get('message', 'Error fetching weather data.')
#             return render(request, 'weather/weather.html', {'error': error_message})
#     return render(request, 'weather/weather.html')

def weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        data = get_weather_data(city)
        if data:
            weather_data = {
                'city': data['city'],
                'temperature': data['temperature'],
                'description': data['description'],
                'icon': data['icon'],  # Pass icon to template
            }
            return render(request, 'weather/weather.html', {'weather': weather_data})
        else:
            error_message = "City not found. Please try again."
            return render(request, 'weather/weather.html', {'error': error_message})
    return render(request, 'weather/weather.html')