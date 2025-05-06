from restaurant import Restaurant, IceCreamStand

applebees = Restaurant('Applebees Bar', 'Ribs')
applebees.describe_restaurant()

baskin_robbins = IceCreamStand('Baskin Robbins', 'Ice Cream')
baskin_robbins.describe_restaurant()

baskin_robbins.list_flavors()