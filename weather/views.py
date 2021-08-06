from django.shortcuts import render
import json
import urllib.request
# Create your views here.


def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


# https://openweathermap.org/api

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                     city+'&appid=f91ce54cd408d000c6313acfd16cbeb7').read()
        json_data = json.loads(res)
        data = {
            "name": str(json_data['name']),
            "country_code": str(json_data['sys']['country']),
            "weather": str(json_data['weather'][0]['description']),
            "coordinate": str(json_data['coord']['lon']) + " " + str(json_data['coord']['lat']),
            "temp": str(int(json_data['main']['temp']) - 273) + get_super('o') + 'C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity'])
        }
    else:
        data = {}
    return render(request, 'index.html', data)
