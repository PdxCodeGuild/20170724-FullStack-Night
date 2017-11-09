#   Lab 11.1.2    Unit Converter


def standardize_inputs(units):
    if units in ['ft', 'foot', 'feet']:  # this is to ensure that whether the user chooses ft or feet, the variable will still be the same
        return 'ft'
    elif units in ['m', 'meter', 'meters']:
        return 'm'
    elif units in ['km', 'kilometer', 'kilometers']:
        return 'km'
    elif units in ['mi', 'mile', 'miles']:
        return 'mi'
    elif units in ['yd', 'yard', 'yds', 'yards']:
        return 'yd'
    elif units in ['in', 'inch', 'inches']:
        return 'in'
    else:
        print('not a known distance.')


def convert_to_meters(distance, from_units):
    if from_units == 'ft':
        return distance * 0.3048
    if from_units == 'mi':
        return distance * 1609.34
    if from_units == 'm':
        return distance * 1
    if from_units == 'km':
        return distance * 1000
    if from_units == 'yd':
        return distance * 0.9144
    if from_units == 'in':
        return distance * 0.0254


def convert_from_meters(distance, to_units):
    if to_units == 'ft':
        return distance / 0.3048
    if to_units == 'mi':
        return distance / 1609.34
    if to_units == 'm':
        return distance / 1
    if to_units == 'km':
        return distance / 1000
    if to_units == 'yd':
        return distance / 0.9144
    if to_units == 'in':
        return distance / 0.0254

def main():
    distance = float(input('What is the distance? '))
    from_units = input('What is the unit you\'d like to convert from? ')
    from_units = standardize_inputs(from_units)
    print('Your distance is ' + str(distance) + ' ' + from_units)

    from_units = standardize_inputs(from_units)

    to_units = input('What would you like to convert this distance to? ')
    to_units = standardize_inputs(to_units)
    print('We are converting ' + str(distance) + ' ' + from_units + ' to ' + to_units)

    distance_in_meters = (convert_to_meters(distance, from_units))
    # print(distance_in_meters)
    print(convert_from_meters(distance_in_meters, to_units))

main()
