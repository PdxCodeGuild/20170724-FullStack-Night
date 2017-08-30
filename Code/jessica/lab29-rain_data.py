import datetime
def parse_csv(path):
    rain = []
    with open('mt_tabor_rain.txt', 'r') as file:
        text = file.read()
        lines = text.split('\n')

        for i in range(12, len(lines)):  # use 12 here to skip over the first 12 lines
            rain_data = lines[i].split()
            rain_data[0] = datetime.datetime.strptime(rain_data[0], '%d-%b-%Y')
            for j in range(1, len(rain_data)):
                if rain_data[j] == '-':
                    rain_data[j] = None
                else:
                    rain_data[j] = int(rain_data[j])
                #print(rain_data[j])
            rain.append(rain_data)
    return rain
parse_csv('mt_tabor_rain.txt')


def mean(data):
    total = 0
    count = 0
    for i in range(len(data)):
        if data[i][1] is not None:
            total += data[i][1]  # data[i] is the data row, data[i][1] is index 1 of data row = daily total
            count += 1
    mean = total / count
    return mean


def variance(data): # difference between the number and mean
    # variance = data[i][1] - mean
    variance_total = 0
    count = 0
    average = mean(data)
    for i in range(len(data)):
        if data[i][1] is not None:
            diff = data[i][1] - average  # don't call mean here because inefficient to loop thru function
            variance_total += diff*diff
            count += 1
    variance = variance_total / count
    return variance


def max_rain(data):
    max_value = float('-inf')
    for i in range(len(data)):
        if data[i][1] is not None:
            if data[i][1] > max_value:
                max_value = data[i][1]
    return max_value


def most_rain_year(data):
    # create a list of averages for each year, # calculate average on per year basis
    years = []
    for i in range(len(data)):
        years.append(data[i][0].year)
    years = list(set(years))
    years.sort()
    print(years)
    return

    counts = [0]*len(years)
    totals = [0]*len(years)

    # counts[i] is the number of records in years[i]
    # totals[i] is the total number of daily totals of the records in years[i]

    # loop through all the data
    # find which year the given record belongs to (data[i][0].year)
    # find the index for that year using years.index(year)
    # increment counts[index]
    # add to totals[index]
    for i in range(len(data)):
        if data[i][1] is not None:
            if data[i][0] == data[i][0].year:

    avg = total / count
    years.append(avg)
    print(years)

    max_year = data[0]
    for i in range(len(years)):
        if data[i] > max_year:
            max_year = data[i]
    print(max_year)


def main():
    rain = parse_csv('mt_tabor_rain.txt')
    #print(mean(rain))
    #print(variance(rain))
    #print(max_rain(rain))
    print(most_rain_year(rain))

main()



