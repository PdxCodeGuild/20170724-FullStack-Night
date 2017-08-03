def convert_to_meters(distance, in_units):
    if in_units == 'feet':
        return distance * 0.0348
    elif in_units == 'miles':
        return distance * 1609.34
    elif in_units == 'kilometers':
        return distance * 1000
    else:
        return distance


def convert_from_meters(distance_in_meters, out_units):
    if out_units == 'feet':
        return distance_in_meters / 0.0348
    elif out_units == 'miles':
        return distance_in_meters / 1609.34
    elif out_units == 'kilometers':
        return distance_in_meters / 1000
    else:
        return distance_in_meters
#conversion:
# feet = 0.0348
# miles = 1609.34
# meters = 1
# kilometer = 1000

while True:
    distance = input('What is the distance? ')
    in_units = input('What are the input units? ')
    out_units = input('What are the output units? ')

    if distance == 'done':
        break
    distance = float(distance)

    distance_in_meters = convert_to_meters(distance, in_units)

    distance_from_meters = convert_from_meters(distance_in_meters, out_units)

    print(distance_from_meters)










