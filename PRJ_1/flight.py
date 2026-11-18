from datetime import datetime


class Flight:

    def __init__(self,flight_number,origin,destination,departure_time,arrival_time,price,capacity):
        if origin == destination:
            raise ValueError("Origin and destination cannot be the same")

        if arrival_time <= departure_time:
            raise ValueError("Arrival time must be after departure time")

        if price <= 0:
            raise ValueError("Invalid flight price")

        if capacity <= 0:
            raise ValueError("Invalid flight capacity")

        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.capacity = capacity
        self.status = "Scheduled"

    def __str__(self):
        return f"{self.flight_number}: {self.origin} -> {self.destination}"