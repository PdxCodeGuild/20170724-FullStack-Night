#   Lab 29  Rain Data


import datetime

import matplotlib.pyplot as plt




def most_rain(rain_data):                   # defines the function to determine the highest value of rain
    max_index = 0                           # initialize max_index to anything

    year_list = []

    for i in range(len(rain_data)):
        year_list.append(rain_data[i][0].year)
    year_list = list(set(year_list))
    year_list.sort()

    totals = [0] * len(year_list)
    counts = [0] * len(year_list)
    averages = []
    for i in range(len(rain_data)):
        if rain_data[i][1] is None:
            continue
        index = year_list.index(rain_data[i][0].year)
        counts[index] += 1
        totals[index] += rain_data[i][1]
    for i in range(len(totals)):
        average = totals[i]/counts[i]
        averages.append(average)

    print(year_list)
    print(totals)
    print(counts)
    print(averages)

    max_average_index = 0
    for i in range(len(averages)):
        if averages[i] > averages[max_average_index]:
            max_average_index = i
    print(max_average_index)
    return year_list, averages, year_list[max_average_index]


def max_daily_rain(rain_data):
    max_index = 0
    for i in range(len(rain_data)):         # i = row of data, loop over the index of the list:rain_data using range(len)) for the whole list
        if rain_data[i][1] is None:         # check if the i = row is None, continue through the loop
            continue
        if rain_data[i][1] > rain_data[max_index][1]:   # check if element 1 (total hours) of the row of i is greater than the element 1 of max_index row
            max_index = i                               # sets variable max_index = index of the greater vale or rain_data[i][1]

    return rain_data[max_index]             # returns the element of rain_data at max_index


def mean_rain(rain_data):                   # defines the function to determine the average of rain in the data set
    count = 0
    sum = 0
    for data_row in rain_data:              # loops over each data_row in the rain_data set
        if data_row[1] is None:             # check if the data row element 1 is None
            continue
        sum += data_row[1]                  # adds each data_row to the sum
        count += 1                          # adds 1 to the count to account for the data rows that are None
    average = sum/count                     # determines the average

    variance_total = 0                      # sets the variance total to 0
    for i in range(len(rain_data)):         # loops through the indices of rain_data
        if rain_data[i][1] == None:         # see above
            continue
        diff = rain_data[i][1] - average    # calculates the difference for each row of datas total rain fall minus the average
        variance_total += diff*diff         # adds the square root of the difference to equal the sum of all variances
    variance = variance_total /count        # calculates the average variance for each data row

    return average, variance


def load(path):
    rain_data = []
    with open(path, 'r') as file:
        text = file.read()                  #text = all characters
        lines = text.split('\n')            #list of lines in text
        for i in range(12, len(lines)):     #loop through lines 12 to end of text
            daily = lines[i].split()        #creates a list called daily and sets each element based of the spaces between
            #print(daily)
            daily[0] = datetime.datetime.strptime(daily[0], '%d-%b-%Y') # first row of data set is the date - uses datetime class to bypass creating strings for dates
            for j in range(1, len(daily)):                              # loops through the elements in daily starting with the first element to the end of the list daily
                if daily[j] == '-':
                    daily[j] = None
                else:
                    daily[j] = int(daily[j])
                    #print(daily[j])

            rain_data.append(daily)

    return rain_data


def main():
    path = 'columbia_ips.rain.txt'
    rain_data = load(path)
    print(rain_data)

    #mean, variance = mean_rain(rain_data)
    #print(mean)
    #print(variance)

    year_list, averages, most_rainy_year = most_rain(rain_data)
    print(f'The rainiest year on average is {most_rainy_year}')

    rain_data_years = []
    rain_data_totals = []

    plt.plot(year_list, averages)
    plt.show()


main()