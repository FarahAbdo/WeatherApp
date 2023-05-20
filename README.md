# WeatherApp
A full weather app code sample using Flask framework and OpenWeatherMap API


In this code sample, we have a Flask app with two routes: `/` and `/result`. The `/` route renders the `index.html` template, which contains a form for the user to enter the name of the city they want to search for. When the form is submitted, the `/result` route is triggered with a POST request, and the weather information for the cityis displayed in the `result.html` template.

The app uses the OpenWeatherMap API to fetch weather data for a given city. The API key is stored in an environment variable for security reasons, and we use the `requests` library to make a GET request to the API endpoint with the city name and the API key as parameters. If the API returns a successful response with a status code of 200, we extract the relevant weather information from the response and store it in a dictionary called `weather`. This dictionary contains the city name, country, temperature, description, and icon code. We then pass this dictionary to the `result.html` template using the `render_template` function.

The HTML templates (`index.html` and `result.html`) use Bootstrap to style the form and the weather information. The templates use Jinja2 syntax to display the dynamic content of the `weather` dictionary.

One important thing to note is that the API key is stored in an environment variable, which is not included in the code. In a real-world scenario, you would need to set the `API_KEY` environment variable before running the app. Moreover, the app does not handle all possible errors or exceptions that may occur when making requests to the API.

Overall, this code sample demonstrates how to build a simple weather app using Flask framework and the OpenWeatherMap API. It also shows how to use HTML templates and Bootstrap to display dynamic content and how to store sensitive information in environment variables for security reasonsOne more thing to note is that the OpenWeatherMap API requires to use HTTPS protocol for API requests. Therefore, you should use `https://` instead of `http://` in the `url` variable to make secure requests to the API endpoint:

```python
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
```

Also, you should handle the case when the city name entered by the user is not found in the API response. In this case, the response will have a status code other than 200, and the `weather` dictionary will not be defined. You can add an `if` statement to check the status code of the response and display an error message in the `index.html` template if the city is not found:

```python
if response.status_code == 200:
    # extract weather information from response
else:
    error_msg = response.json()['message']
    return render_template('index.html', error_msg=error_msg)
```

```html
{% if error_msg %}
    <div class="error-msg">{{ error_msg }}</div>
{% endif %}
```
