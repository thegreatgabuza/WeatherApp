from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city_name = request.form.get('city')

        #take a variable to show the json data
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=5ffca268fa0f06daf562e2aa72761113')

        #read the json object
        json_object = r.json()

        #take some attributes like temperature,humidity,pressure of this
        temperature = int(json_object['main']['temp']-273.15) #this temparetuure in kelvin
        humidity = int(json_object['main']['humidity'])
        pressure = int(json_object['main']['pressure'])
        wind = int(json_object['wind']['speed'])

        #atlast just pass the variables
        condition = json_object['weather'][0]['main']
        desc = json_object['weather'][0]['description']

        return render_template('home.html',temperature=temperature,pressure=pressure,humidity=humidity,city_name=city_name,condition=condition,wind=wind,desc=desc)
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
