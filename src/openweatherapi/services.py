import httpx
from settings import settings


async def get_weather_by_city_name(city_name):
    """ Получение данных  о погоде с помощью OpenWeatherAPI"""
    parameters = {
        'appid': settings.OPENWEATHER_API_KEY,
        'units': 'metric',
        'lang': 'ru',
        'q': city_name
    }
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.openweathermap.org/data/2.5/weather', params=parameters)

    if not response.status_code == 200:
        return None
    data = response.json()
    message = f'''В городе <b>{data['name']}</b>  
            <i>{data['weather'][0]['description'].capitalize()}</i>,
            температура воздуха: {data['main']['temp']} градусов по Цельсию,
            Скорость ветра {data['wind']['speed']} м/с
                    '''
    return message

