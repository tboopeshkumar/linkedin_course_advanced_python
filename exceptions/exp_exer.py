class InvalidTempError(Exception):
    """Raised when an invalid temperature is set"""
    def __init__(self, temp):
        super().__init__(f"Invalid temperature: {temp}")

class DigitalOven:
    def __init__(self):
        self.temp = 0
    
    def set_temp(self, temp):
        if temp != 0 and (temp < 100 or temp > 500):
            raise InvalidTempError(temp)
        self.temp = temp

    def get_temp(self):
        return self.temp

def test_oven(test_temp):
    global test_oven
    try:
        oven.set_temp(test_temp)
    except InvalidTempError as e:
        print(e)
    else:
        print("Temperature set to", oven.get_temp())
    finally:
        print("Current temperature setting is", oven.get_temp())

oven = DigitalOven()
test_oven(200)
test_oven(50)
test_oven(0)
test_oven(600)