from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup as bs


# Create your views here.
def get_weather_data(city):
    city = city.replace(' ','+')
    url = f"https://www.google.com/search?q=weather+of+{city}"
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
    LANGUAGE = 'en-GB,en;q=0.9,en-US;q=0.8'
    session = requests.Session()
    session.headers['user-agent'] = USER_AGENT
    session.headers['accept-language'] = LANGUAGE
    response = session.get(url)
    soup = bs(response.text, 'html.parser')
    # Extract_region
    result = {}
    result['region'] = soup.find('span', attrs={'class':'BBwThe'}).text
    result['day_time'] = soup.find('div', attrs={'id':'wob_dts'}).text
    result['weather'] = soup.find('span', attrs={'id':'wob_dc'}).text
    result['temperature']= soup.find('span', attrs={'id':'wob_tm'}).text
    # print(result)
    return result

def home_view(request):
    if request.method == 'GET' and 'city' in request.GET:
        city = request.GET.get('city')
        result = get_weather_data(city)
        context = {'result':result}
    else:
        context = {}
    return render(request, 'weatherap/home.html', context)











