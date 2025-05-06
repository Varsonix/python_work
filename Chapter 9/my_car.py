from car import Car

my_new_car = Car('Subaru', 'Impreza WRX', '2004')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 24_430
my_new_car.read_odometer()