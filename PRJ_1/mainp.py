from user import User
from connect_db import ConnectDB
from api import Getapi
from datetime import datetime , timedelta



class AirlineSystem(ConnectDB):
    def __init__(self):
        self.user = User()
        self.api = Getapi()


    def main_menu(self):
        print("*** Airline Ticket System ***")
        print("1. Register")
        print("2. User Login")
        print("3. Admin Login ")
        print("0. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            self.register()
        elif choice == "2":
            self.user_login()
        elif choice == "3":
            self.admin_login()
        elif choice == "0":
            print("Goodbye")


    def register(self):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        username = input("Username: ")
        password = input("Password: ")
        self.user.register(first_name, last_name, username, password)
        print("Registration completed!")
        self.user_login()


    def user_login(self):
        username = input("Username: ")
        password = input("Password: ")
        user = self.user.login(username, password)
        if user:
            self.current_user = user
            print("Login successful!")
            self.user_panel()
        else:
            print("Invalid username or password!")


    def user_panel(self):
        while True:
            print("*** User Panel ***")
            print("1. View Flights")
            print("2. Wallet")
            print("3. Increase balance")
            print("4. By Ticket")
            print("5. My Ticket")
            print("6. Change Password")
            print("0. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.view_flights()
            elif choice == "2":
                self.wallet()
            elif choice == "3":
                self.top_up_wallet()
            elif choice == "4":
                self.buy_ticket()
            elif choice == "5":
                self.my_tickets()
            elif choice == "6":
                self.change_password()
            elif choice == "0":
                break

   
    def view_flights(self):
        query = "SELECT * FROM flights"
        with self.user.con.cursor() as cursor:
            cursor.execute(query)
            flights = cursor.fetchall()
        for flight in flights:
            print(flight)
            self.api.get_weather(flight[3])


    def wallet(self):
        print("*** Wallet ***")
        print(f"Your balance: {self.current_user[6]}")        


    def top_up_wallet(self):
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Invalid amount!")
            return
        query = """
            UPDATE users
            SET balance = balance + %s
            WHERE id = %s
        """
        with self.user.con.cursor() as cursor:
            cursor.execute(query, (amount, self.current_user[0]))

            query = """
                INSERT INTO transactions (user_id, amount, type)
                VALUES (%s, %s, %s)
                """
            cursor.execute(query, (self.current_user[0], amount, "deposit"))
        self.user.con.commit()
        print("Wallet charged successfully!")


    def buy_ticket(self):
        flight_number = input("Enter flight number: ")

        query = """
            SELECT * FROM flights
            WHERE flight_number = %s
        """

        with self.user.con.cursor() as cursor:
            cursor.execute(query, (flight_number,))
            flight = cursor.fetchone()

        if not flight:
            print("Flight not found!")
            return

        if flight[8] != "active":
            print("This flight is not available!")
            return

        if flight[9] >= flight[7]:
            print("No seats available!")
            return

        if self.current_user[6] < flight[6]:
            print("Insufficient wallet balance!")
            return

        try:
            with self.user.con.cursor() as cursor:

                query = """
                    SELECT id, seat_number, seat_class
                    FROM seats
                    WHERE flight_id = %s AND is_booked = FALSE
                    ORDER BY id
                    LIMIT 1
                    FOR UPDATE
                """
                cursor.execute(query, (flight[0],))
                seat = cursor.fetchone()

                if not seat:
                    print("No seats available!")
                    self.user.con.rollback()
                    return

                query = """
                    INSERT INTO tickets
                    (username, flight_number, purchase_time, price, seat_id)
                    VALUES (%s, %s, CURRENT_TIMESTAMP, %s, %s)
                """
                cursor.execute(query, (
                    self.current_user[3],
                    flight[1],
                    flight[6],
                    seat[0]
                ))

                query = """
                    UPDATE seats
                    SET is_booked = TRUE
                    WHERE id = %s
                """
                cursor.execute(query, (seat[0],))

                query = """
                    UPDATE users
                    SET balance = balance - %s
                    WHERE id = %s
                """
                cursor.execute(query, (flight[6], self.current_user[0]))

                query = """
                    UPDATE flights
                    SET booked_seats = booked_seats + 1
                    WHERE id = %s
                """
                cursor.execute(query, (flight[0],))

                query = """
                    INSERT INTO transactions (user_id, amount, type)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(query, (
                    self.current_user[0],
                    flight[6],
                    "purchase"
                ))

            self.user.con.commit()
            print(f"Ticket purchased successfully! Seat: {seat[1]} ({seat[2]})")

        except Exception as e:
            self.user.con.rollback()
            print("Ticket purchase failed!")
            print(e)


    def cancel_ticket(self):
        query = """
            SELECT * FROM tickets
            WHERE username = %s
        """
        with self.con.cursor() as cursor:
            cursor.execute(query, (self.current_user[3],))
            tickets = cursor.fetchall()
            for ticket in tickets:
                print(f"Ticket ID: {ticket[0]} | Flight: {ticket[2]} | Price: {ticket[4]} | Status: {ticket[6]}")

        ticket_id = int(input("Input ticket_id: "))
        query = """
            SELECT * FROM tickets
            WHERE id = %s AND username = %s
        """
        with self.con.cursor() as cursor:
            cursor.execute(query, (ticket_id, self.current_user[3]))
            ticket = cursor.fetchone()
        if not ticket:
            print("Ticket not found!")
            return
        if ticket[6] != "PAID":
            print("This ticket cannot be cancelled!")
            return

        query = """
            SELECT departure_time FROM flights
            WHERE flight_number = %s
        """
        with self.con.cursor() as cursor:
            cursor.execute(query, (ticket[2],))
            flight = cursor.fetchone()

        if flight[0] <= datetime.now() + timedelta(hours=24):
            print("Ticket cancellation time has expired!")
            return

        query = """
            UPDATE tickets
            SET status = 'CANCELLED'
            WHERE id = %s
        """
        with self.con.cursor() as cursor:
            cursor.execute(query, (ticket_id,))

        refund_amount = ticket[4] * 0.8
        query = """
            UPDATE users
            SET balance = balance + %s
            WHERE id = %s
        """
        with self.con.cursor() as cursor:
            cursor.execute(query, (refund_amount, self.current_user[0]))

        self.con.commit()
        print("Ticket cancelled successfully!")          

        query = """
            INSERT INTO transactions (user_id, amount, type)
            VALUES (%s, %s, %s)
        """
        with self.con.cursor() as cursor:
            cursor.execute(query, (
                self.current_user[0],
                refund_amount,
                "refund"
            ))
                    

    def my_tickets(self):
        query = """
            SELECT * FROM tickets
            WHERE username = %s
        """

        with self.user.con.cursor() as cursor:
            cursor.execute(query, (self.current_user[3],))
            tickets = cursor.fetchall()

        if not tickets:
            print("You have no tickets!")
            return
        print("*** My Tickets ***")
        for ticket in tickets:
            print(ticket)


    def transaction_history(self):
        query = """
            SELECT amount, type, created_at
            FROM transactions
            WHERE user_id = %s
        """
        with self.user.con.cursor() as cursor:
            cursor.execute(query, (self.current_user[0],))
            transactions = cursor.fetchall()

            for transaction in transactions:
                print(f"Amount: {transaction[0]} | Type: {transaction[1]} | Date: {transaction[2]}")


    def change_password(self):
        pass

#-------------------admin------------------------------


    def admin_login(self):
        username = input("usernamr: ")
        password = input("password: ")
        admin = self.user.login(username,password)
        if admin and admin[5] == True:
            print("Admin login successful!")
            self.current_admin = admin
            self.admin_panel()
        else:
            print("Invalid username or password") 


    def admin_panel(self):
        while True:
            print("*** Admin Panel ***")
            print("1. View Users")
            print("2. Manage Airports")
            print("3. Manage Flights")
            print("0. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.view_users()
            elif choice == "2":
                self.ManageAirport()
            elif choice == "3":
                self.ManageFlight()
            elif choice == "0":
                break


    def ManageAirport(self):
        while True:
            print("1. Add Airport")
            print("2. Update Airport")
            print("3.Delete Airport")
            print("4. view airport")
            print("0. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.add_airport()
            elif choice == "2":
                self.update_airport()
            elif choice == "3":
                self.delete_airport()
            elif choice == "4":
                self.view_airports()
            elif choice == "0":
                break


    def ManageFlight(self):
        while True:
            print("1. Add Flight")
            print("2. Update Flight")
            print("3.Delete Flight")
            print("4. view flight")
            print("0. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.add_flight()
            elif choice == "2":
                self.update_flight()
            elif choice == "3":
                self.delete_flight()
            elif choice == "4":
                self.view_flights()
            elif choice == "0":
                break


    def view_users(self):
        query = "SELECT * FROM users"
        with self.user.con.cursor() as cursor:
            cursor.execute(query)
            users = cursor.fetchall()
        for user in users:
            print(user)
        


    def view_airports(self):
        query = "SELECT * FROM airports"
        with self.user.con.cursor() as cursor:
            cursor.execute(query)
            airports = cursor.fetchall()
        for airport in airports:
            print(airport)


    def add_airport(self):
        code = input("Airport code: ")
        name = input("Airport name: ")
        city = input("City: ")
        country = input("Country: ")
        latitude = float(input("Latitude: "))
        longitude = float(input("Longitude: "))

        query = """
            INSERT INTO airports (code, name, city, country, latitude, longitude)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        with self.user.con.cursor() as cursor:
            cursor.execute(query, (code, name, city, country, latitude, longitude))

        self.user.con.commit()
        print("Airport added successfully!")


    def update_airport(self):
        code = input("Enter airport code: ")
        name = input("New airport name: ")
        city = input("New city: ")
        country = input("New country: ")
        latitude = float(input("New latitude: "))
        longitude = float(input("New longitude: "))

        query = """
            UPDATE airports
            SET name = %s, city = %s, country = %s,
                latitude = %s, longitude = %s
            WHERE code = %s
        """

        with self.user.con.cursor() as cursor:
            cursor.execute(query, (name, city, country, latitude, longitude, code))

        self.user.con.commit()
        print("Airport updated successfully!")


    def delete_airport(self):
        code = input("Enter airport code: ")

        query = "DELETE FROM airports WHERE code = %s"

        with self.user.con.cursor() as cursor:
            cursor.execute(query, (code,))

        self.user.con.commit()
        print("Airport deleted successfully!")
        

    def add_flight(self):
        flight_number = input("Flight number: ")
        origin = input("Origin airport: ")
        destination = input("Destination airport: ")
        departure = input("Departure time (YYYY-MM-DD HH:MM): ")
        arrival = input("Arrival time (YYYY-MM-DD HH:MM): ")
        price = float(input("Price: "))
        capacity = int(input("Capacity: "))

        query = """
            INSERT INTO flights
            (flight_number, origin_airport, destination_airport,
            departure_time, arrival_time, price, capacity)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        with self.user.con.cursor() as cursor:
            cursor.execute(query, (
                flight_number, origin, destination,
                departure, arrival, price, capacity
            ))

        self.user.con.commit()
        print("Flight added successfully!")


    def update_flight(self):
        flight_number = input("Enter flight number: ")
        origin = input("New origin airport: ")
        destination = input("New destination airport: ")
        departure = input("New departure time: ")
        arrival = input("New arrival time: ")
        price = float(input("New price: "))
        capacity = int(input("New capacity: "))
        status = input("New status: ")

        query = """
            UPDATE flights
            SET origin_airport = %s,
                destination_airport = %s,
                departure_time = %s,
                arrival_time = %s,
                price = %s,
                capacity = %s,
                status = %s
            WHERE flight_number = %s
        """

        with self.user.con.cursor() as cursor:
            cursor.execute(query, (
                origin, destination, departure,
                arrival, price, capacity, status,
                flight_number
            ))

        self.user.con.commit()
        print("Flight updated successfully!")


    def delete_flight(self):
        flight_number = input("Enter flight number: ")

        query = """
            DELETE FROM flights
            WHERE flight_number = %s
        """

        with self.user.con.cursor() as cursor:
            cursor.execute(query, (flight_number,))

        self.user.con.commit()
        print("Flight deleted successfully!")






app = AirlineSystem()
app.main_menu()

