from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metrics&appid=7d2dd36bd23a52dff6c24aaa9edb067b').read()
        list_data = json.loads(source)
        data = {
            "country_code" : str(list_data['sys']['country']),
            "coordinate"   : str(list_data['coord']['lon']) + str(list_data['coord']['lat']),
            "temp"         : str(list_data['main']['temp']) + '°C',
            "pressure"     : str(list_data['main']['pressure']),
            "humidity"     : str(list_data['main']['humidity']),
            "main"         : str(list_data['weather'][0]['main']),
            "description"  : str(list_data['weather'][0]['description']),
            "icon"         : str(list_data['weather'][0]['icon']),
        }
        print(data)
    else:
         data = {}
    return render(request,"main/index.html",data)        
