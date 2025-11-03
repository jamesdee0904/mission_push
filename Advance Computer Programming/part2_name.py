class KelvinConverter: 
    def __init__(self, celsius_list):
        self.celsius_list = celsius_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.celsius_list):
            kelvin = self.celsius_list[self.index] + 273.15
            self.index += 1
            return round(kelvin, 2)
        else:
            raise StopIteration


def fahrenheit_converter(celsius_list):
    for temp in celsius_list:
        fahrenheit = (temp * 9/5) + 32
        yield round(fahrenheit, 2)


def main():
    celsius_temps = [25, 30, 15, 0, -5, 40]  

    print("Celsius value from file:", celsius_temps)
    print()
    
    kelvin_temps = KelvinConverter(celsius_temps)
    print("Converted to Kelvin using Iterator:")
    for temp in kelvin_temps:
        print(temp)
    
    fahrenheit_temps = fahrenheit_converter(celsius_temps)
    print()
    print("Converted to Fahrenheit using Generator:")
    for temp in fahrenheit_temps:
        print(temp)


if __name__ == '__main__':
    main()
