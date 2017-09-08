city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}


def one_hop(city):
    # prints all cities connected to city chosen
    return city_to_accessible_cities[city]


def two_hops(city):
    all_cities_reached = []
    for one_hop_city in city_to_accessible_cities[city]:
        all_cities_reached.extend(city_to_accessible_cities[one_hop_city])
        all_cities_reached = list(set(all_cities_reached))
    return all_cities_reached


def n_hops(city, hops):
    count = 0
    all_cities_reached = []
    while count < hops:
        for one_hop_city in city_to_accessible_cities[city]:
            all_cities_reached.extend(city_to_accessible_cities[one_hop_city])
            all_cities_reached = list(set(all_cities_reached))
            count += 1
    return all_cities_reached


def n_hops2(city, hops):  # use recursion
    all_cities_reached = []
    if hops == 1:
        return list(city_to_accessible_cities[city])
    for one_hop_city in city_to_accessible_cities[city]:
        accessible_cities = n_hops2(one_hop_city, hops - 1)
        all_cities_reached.extend(accessible_cities)
        all_cities_reached = list(set(all_cities_reached))
    return all_cities_reached


def factorial(n): # example of recursion
    if n == 0:
        return 1
    return n*factorial(n-1)


def shortest_travel(city, hops):
    all_cities_reached = []
    if hops == 1:
        return list(city_to_accessible_cities_with_travel_time[city])
    for one_hop_city in city_to_accessible_cities_with_travel_time[city]:
        accessible_cities = n_hops2(one_hop_city, hops - 1)

    return all_cities_reached


def main():
    city = input('Enter a city: ')
    hops = int(input('Enter the number of hops: '))

    #print(one_hop(city))
    #print(two_hops(city))
    #print(n_hops2(city, hops))
    print(shortest_travel(city, hops))
main()





