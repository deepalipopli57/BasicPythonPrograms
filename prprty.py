class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

a = Celsius()
a.temperature = 37
print(a.temperature)
print(a.to_fahrenheit())
print(a.__dict__)

#Using setters and getters
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_farhn(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Get temp")
        return self._temperature

    @temperature.setter
    def temperature(self, val):
        if val < -273:
            raise ValueError("Wrong temp")
        print("Set value")
        self._temperature = val

a = Celsius(-400)
a.temprature = 39
print(a.temprature)
print(a.to_farhn())

"""
Without property
    class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)
"""

