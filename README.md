WeatherApp is a Flask web application that provides weather information for a given location using the OpenWeather API. This project demonstrates how to build a simple web application with Flask and integrate it with an external API to fetch and display data.

Table of Contents
Installation
Usage
Project Structure
How It Works
Example Code
Contributing
License
Contact
Acknowledgements
Installation
Clone the repository:
git clone https://github.com/thegreatgabuza/WeatherApp.git
cd WeatherApp
Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:
pip install -r requirements.txt
Obtain an API key from OpenWeather and add it to your environment variables:
export OPENWEATHER_API_KEY='your_api_key'  # On Windows use `set OPENWEATHER_API_KEY=your_api_key`
Usage
Run the Flask application:
flask run
Open your web browser and navigate to http://127.0.0.1:5000.
Enter a location in the search box and click "Get Weather" to see the current weather information for that location.

How It Works
Flask Application: The application is built using the Flask framework.
OpenWeather API: The app fetches weather data from the OpenWeather API based on the user's input location.
HTML Template: The weather information is displayed using an HTML template.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Fork the Project.
Create your Feature Branch:
git checkout -b feature/AmazingFeature
Commit your Changes:
git commit -m 'Add some AmazingFeature'
Push to the Branch:
git push origin feature/AmazingFeature
Open a Pull Request.
License
Distributed under the MIT License. See LICENSE for more information.

Acknowledgements
Flask: For providing a simple and powerful web framework.
OpenWeather: For offering a comprehensive weather API.
Bootstrap: For providing a responsive design framework (if used).

