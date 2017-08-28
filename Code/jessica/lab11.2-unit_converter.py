while True:
    input_distance = input('What is the distance? ')
    units = input('What are the units? ')

    if input_distance == 'done':
        break
    distance = float(input_distance)
    if units == 'foot' or units == 'feet':
        print(str(distance) + ' ' + units + ' is ' + str(distance * 0.3048) + ' meters')
    elif units == 'mile' or units == 'miles':
        print(str(distance) + ' ' + units + ' is ' + str(distance * 1609.34) + ' meters')
    elif units == 'meter' or units == 'meters':
        print(str(distance) + ' ' + units + ' is ' + str(distance) + ' meters')
    elif units == 'kilometer' or units == 'kilometers':
        print(str(distance) + ' ' + units + ' is ' + str(distance * 1000) + ' meters')



