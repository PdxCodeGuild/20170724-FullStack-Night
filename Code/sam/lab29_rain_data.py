import datetime
import matplotlib.pyplot as plt

def load(path):
    data = []
    with open(path, 'r') as file:
        text = file.read()
        lines = text.split('\n')

        for i in range(12, len(lines)):                                     # iterate over lines in text, skipping first 12 lines
            data_row = []                                                   # create an empty list for data rows
            split_line = lines[i].split()                                   # split lines at white space
            date = datetime.datetime.strptime(split_line[0], '%d-%b-%Y')    # convert date strings into datetime objects
            data_row.append(date)                                           # append date time objects to data_row
            for j in range(1, len(split_line)):                             # iterate over split_lines, skipping date
                data_row.append(int(split_line[j]))                         # convert data into ints, append to data_row
            data.append(data_row)                                           # append data_row to data to create a list of lists
    return data


def mean(data):
    total = 0                                                               # running total
    for i in range(len(data)):
        total += data[i][1]                                                 # add data[i][1] (daily total) to total
    av = total / len(data)
    return av


def variance(data, av):                                                     # function to calculate variance
    total = 0
    for i in range(len(data)):
        diff = data[i][1] - av                                              # difference = daily total - average
        total += diff * diff                                                # add the square of difference to total
    variance = total / len(data)
    return variance


def most_rainy_day(data):                                                   # function to calculate the day with the most rain on average
    max_index = 0
    for i in range(len(data)-1):
        if data[i][1] > data[max_index][1]:                                 # if daily total at data[i] is greater than daily total at data[max_index]
            max_index = i                                                   # change max index to data[i]
    return data[max_index]


def most_rainy_year(data):                                                  # function to calculate year with most rainfall on average
    all_years = []                                                          # empty list to append all years to
    for i in range(len(data)):
        all_years.append(data[i][0].year)
    years_set = set(all_years)                                              # convert all_years into a set
    years = list(sorted(years_set))                                         # convert set back into a list and sort it
    totals = [0]*len(years)                                                 # create a list of zeros, the length of list of years
    counts = [0]*len(years)

    for i in range(len(data)):
        year = data[i][0].year
        index = years.index(year)
        totals[index] += data[i][1]
        counts[index] += 1

    averages = []
    for i in range(len(totals)):
        averages.append(totals[i] / counts[i])                              # append (totals[i] / counts[i]) to averages

    max_index = 0
    for i in range(len(averages)-1):
        if averages[i] > averages[max_index]:                               # if averages[i] greater than averages[max_index]
            max_index = i                                                   # set max_index to i (highest average)
    return years[max_index]                                                 # returning the year with the highest av rainfall


def longest_period_of_continuous_rain(data):
    longest_stretch = 0
    current_stretch = 0
    for i in range(len(data)):
        if data[i][1] is None:
            continue
        if data[i][1] == 0:
            if current_stretch > longest_stretch:
                longest_stretch = current_stretch
                current_stretch = 0
            else:
                current_stretch += 1
    return longest_stretch



def yearly_averages(data):
    all_years = []
    for i in range(len(data)):
        all_years.append(data[i][0].year)
    years_set = set(all_years)
    years = list(sorted(years_set))
    totals = [0] * len(years)
    counts = [0] * len(years)

    for i in range(len(data)):
        year = data[i][0].year
        index = years.index(year)
        totals[index] += data[i][1]
        counts[index] += 1

    averages = []
    for i in range(len(totals)):
        averages.append(totals[i] / counts[i])
    return averages


def years_sorted(data):
    all_years = []
    for i in range(len(data)):
        all_years.append(data[i][0].year)
    years_set = set(all_years)
    years = list(sorted(years_set))
    return years


def main():
    data = load('hayden_island.txt')
    av = mean(data)

    # creating graph using matplotlib
    x_values = years_sorted(data)
    y_values = yearly_averages(data)
    plt.plot(x_values, y_values)
    plt.show()

    print(mean(data))
    print(variance(data, av))
    print(most_rainy_day(data))
    print(most_rainy_year(data))
    print(longest_period_of_continuous_rain(data))

main()