
def accessible_cities(user_input, city_to_accessible_cities):
    return list(city_to_accessible_cities[user_input])


def two_hops(accessible, city_to_accessible_cities):
    two_hops_away = []
    for city in accessible:
        two_hops_away.extend(city_to_accessible_cities[city])
    return list(set(two_hops_away))


def user_hops(accessible, city_to_accessible_cities, n_hops):
    cities = []
    i = 0
    while i < n_hops:
        for city in accessible:
            cities.extend(city_to_accessible_cities[city])
    i += 1
    return cities



def main():

    city_to_accessible_cities = {
      'Boston': {'New York', 'Albany', 'Portland'},
      'New York': {'Boston', 'Albany', 'Philadelphia'},
      'Albany': {'Boston', 'New York', 'Portland'},
      'Portland': {'Boston', 'Albany'},
      'Philadelphia': {'New York'}
    }

    user_input = input('Please select a city you would like to travel to from the following cities: Boston, New York, Albany, Portland, Philadelphia. ')
    n_hops = int(input('Input the number of "hops" you would like to take'))

    accessible = accessible_cities(user_input, city_to_accessible_cities)

    print('Great! the following cities located one "hop" away! ' + str(user_input) + ': ' + str(accessible))
    print('These are the cities located two "hops" away!' + str(two_hops(accessible, city_to_accessible_cities)))
    print(user_hops(accessible, city_to_accessible_cities, user_input2 ))


main()