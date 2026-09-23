class PereatedNumber(Exception):
    def __init__(self, *args):
        self.message="the number is repeated"
        super().__init__(self.message,*args)
class RepeatedCar(Exception):
    def __init__(self, *args):
        self.message="the car is in parking now"
        super().__init__(self.message*args)

class InvalidCar(Exception):
    def __init__(self, *args):
        self.massage = "the car does not exist"
        super().__init__(self.massage,*args)

class ExitedCar(Exception):
    def __init__(self, *args):
        self.massage = "the car is not parking"
        super().__init__(self.massage,*args)

class OccupiedSpace(Exception):
    def __init__(self, *args):
        self.massage = "the space is not Occupied"
        super().__init__(self.massage,*args)

class RepetedSubscription(Exception):
    def __init__(self, *args):
        self.massage = "the Subscription is not valid or repeted"
        super().__init__(self.massage,*args)

class InvalidExitTime(Exception):
    def __init__(self, *args):
        self.massage = "the car did not enter yet"
        super().__init__(self.massage,*args)

