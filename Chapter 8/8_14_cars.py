def make_car(make, model, **car_info):
    """Build a car based on the supplied information"""
    car_info['make'] = make.title()
    car_info['model'] = model.title()
    return car_info

car = make_car(
    'Subaru',
    'Impreza WRX',
    year='2004',
    miles=143000,
    color='blue',
    transmission='manual'
)

print(car)