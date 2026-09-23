from abc import ABC


class Drone(ABC):

    AVAILABLE = "AVAILABLE"
    IN_MISSION = "IN_MISSION"
    CHARGING = "CHARGING"
    MAINTENANCE = "MAINTENANCE"

    def __init__(self, drone_id, name, battery=100):
        self.drone_id = drone_id
        self.name = name
        self.battery = battery
        self.status = self.AVAILABLE
        self.successful_missions = 0

    def can_start(self):

        if self.status != self.AVAILABLE:
            return False

        if self.battery < 20:
            return False

        return True

    def start(self):

        if self.can_start():
            self.status = self.IN_MISSION
            return True

        return False

    def finish(self, success=True):

        self.status = self.AVAILABLE

        if success:
            self.successful_missions += 1

    def charge(self):

        if self.status == self.MAINTENANCE:
            return False

        self.status = self.CHARGING
        self.battery = 100
        self.status = self.AVAILABLE

        return True

    def send_to_maintenance(self):
        self.status = self.MAINTENANCE

    def finish_maintenance(self):
        self.status = self.AVAILABLE




class EquipmentDrone(Drone):

    def __init__(self, drone_id, name, max_capacity, battery=100):
        super().__init__(drone_id, name, battery)
        self.max_capacity = max_capacity




class SearchDrone(Drone):

    def __init__(self, drone_id, name, battery=100):
        super().__init__(drone_id, name, battery)

        self.search_areas = [
            "SMALL",
            "MEDIUM",
            "LARGE"
        ]


class MedicalDrone(Drone):

    def __init__(
        self,
        drone_id,
        name,
        can_carry_critical=False,
        battery=100
    ):
        super().__init__(drone_id, name, battery)

        self.can_carry_critical = can_carry_critical




class User(ABC):

    def __init__(self, user_id, name, username, password):

        if len(password) < 8:
            raise ValueError(
                "Password must have at least 8 characters"
            )

        self.user_id = user_id
        self.name = name
        self.username = username

        # Password is private
        self.__password = password

        self.active = True

    def check_password(self, password):
        return self.__password == password

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False




class Operator(User):

    def __init__(self, user_id, name, username, password):

        super().__init__(
            user_id,
            name,
            username,
            password
        )



class Admin(User):

    def __init__(self, user_id, name, username, password):

        super().__init__(
            user_id,
            name,
            username,
            password
        )

    def send_drone_to_maintenance(self, drone):

        if not self.active:
            return False

        drone.send_to_maintenance()

        return True

    def finish_drone_maintenance(self, drone):

        if not self.active:
            return False

        drone.finish_maintenance()

        return True