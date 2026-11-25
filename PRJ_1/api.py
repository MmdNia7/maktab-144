from connect_db import ConnectDB
import requests




class Getapi(ConnectDB):

    def get_weather(self, destination):
        query = """
            SELECT latitude, longitude
            FROM airports
            WHERE name = %s
        """
        with self.con.cursor() as cursor:
            cursor.execute(query, (destination,))
            coordinates = cursor.fetchone()

        if not coordinates:
            print("Airport not found!")
            return

        latitude = coordinates[0]
        longitude = coordinates[1]

        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            weather = response.json()
            print(f'temperature: {weather["current"]["temperature_2m"]}')
            print(f'relative_humidity: {weather["current"]["relative_humidity_2m"]}')
            print(f'wind_speed: {weather["current"]["wind_speed_10m"]}')
            print(f'Weather time: {weather["current"]["time"]}')

        except requests.exceptions.Timeout:
            print("Time is up")
        except requests.exceptions.RequestException:
            print("Connection error!")

    
