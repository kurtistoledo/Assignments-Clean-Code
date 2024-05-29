# Lesson 4: Clean Code
# 2. Refactoring a Weather Forecast Application into Classes and Modules

class WeatherFetcher:
    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        weather_data = {
            "New York": {"city": "New York", "temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"city": "London", "temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"city": "Tokyo", "temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        return weather_data.get(city, {})

class WeatherParser:
    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class WeatherApp:
    def __init__(self):
        self.fetcher = WeatherFetcher()
        self.parser = WeatherParser()

    def get_detailed_forecast(self, city):
        data = self.fetcher.fetch_weather_data(city)
        return self.parser.parse_weather_data(data)

    def display_weather(self, city):
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse_weather_data(data)
            print(weather_report)

    def run(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                self.display_weather(city)
                forecast = ""
            print(forecast)

if __name__ == "__main__":
    app = WeatherApp()
    app.run()
