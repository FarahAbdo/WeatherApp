from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        api_key = os.environ['API_KEY']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url).json()
        if response['cod'] == 200:
            weather = {
                'city': response['name'],
                'country': response['sys']['country'],
                'temperature': round(response['main']['temp']),
                'description': response['weather'][0]['description'].title(),
                'icon': response['weather'][0]['icon']
            }
            return render_template('result.html', weather=weather)
        else:
            error_msg = response['message']
            return render_template('index.html', error_msg=error_msg)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
