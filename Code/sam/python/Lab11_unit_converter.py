

# converting units given to meters
def convert_to_meters(distance, from_units):
    if from_units == 'inch':
        return distance * 0.0254
    elif from_units == 'ft':
        return distance * 0.305
    elif from_units == 'yd':
        return distance * 0.914
    elif from_units == 'mi':
        return distance * 1609.34
    elif from_units == 'km':
        return distance * 1000
    elif from_units == 'm':
        return distance


def convert_from_meters(distance_in_meters, to_units):
    if to_units == 'inch':
        return distance_in_meters / 0.0254
    elif to_units == 'ft':
        return distance_in_meters / 0.305
    elif to_units == 'yd':
        return distance_in_meters / 0.914
    elif to_units == 'mi':
        return distance_in_meters / 1609.34
    elif to_units == 'km':
        return distance_in_meters / 1000
    elif to_units == 'm':
        return distance_in_meters


from_units = input('Enter unit of measurement you wish to convert (inch, ft, yd, mi, km, or m ): ')
distance = float(input('Enter distance: '))
to_units = input('Enter unit of measurement you wish to convert to (inch, ft, yd, mi, km or m ): ')


distance_in_meters = convert_to_meters(distance, from_units)
distance_from_meters = convert_from_meters(distance_in_meters, to_units)

output = str(distance) + from_units + ' is ' + str(distance_from_meters) + to_units

print(output)





