class Airport:

    def __init__(self, id, name, city, country, latitude, longitude):
        self.code = id
        self.name = name
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"{self.id} - {self.name} ({self.city}, {self.country})"