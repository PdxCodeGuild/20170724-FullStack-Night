import datetime
import matplotlib.pyplot as plt

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
    avg = total / count
    return avg


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
    var = variance_total / count
    return var


def max_rain(data):
    # max_value = float('-inf')
    # for i in range(len(data)):
    #     if data[i][1] is not None:
    #         if data[i][1] > max_value:
    #             max_value = data[i][1]
    # return max_value returns the value to return the day see below

    max_index = 0
    for i in range(len(data)):
        if data[i] > data[max_index]:
            max_index = i
    return data[max_index][0]

'''
class YearlyAverage:
    def __init(self, year):
        self.year = year
        self.total = 0
        self.count = 0
yearly_averages = [YearlyAverage(1998), YearlyAverage(1999)]
for i in range(len(data)):
    year = data[i][0].year
    for j in range(len(yearly_averages)):
        if yearly_averages[j].year == year:
            yearly_averages[j].count += 1
            break
average_for_1998 = yearly_averages[0].total / yearly_averages.count
'''





def most_rain_year(data):
    # create a list of averages for each year, # calculate average on per year basis
    years = []
    for i in range(len(data)):
        years.append(data[i][0].year)
    years = list(set(years))
    years.sort()


    '''total_1998 = 0
    count_1998 = 0
    total_1999 = 0
    count_1999 = 0
    for i in range(len(data)):
        if data[i][1] is None:
            continue
        year = data[i][0].year
        if year == 1998:
            total_1998 += data[i][1]
            count_1998 += 1
        elif year == 1999:
            total_1999 += data[i][1]
            count_1999 += 1
    average_1998 = total_1998 / count_1998'''



    #stats = [[2000, 0, 0],[2001, 0, 0],[2002, 0, 0],[2003, 0, 0]]
    #[2000, 2001, ...]
    #[0, 0, ...]
    #[0, 0, ...]

    counts = [0]*len(years)  # counts[i] is the number of records in years[i]
    totals = [0]*len(years)  # totals[i] is the total number of daily totals of the records in years[i]


    #  loop through all the data
    # find which year the given record belongs to (data[i][0].year)
    # find the index for that year using years.index(year)
    # increment counts[index]
    # add to totals[index]
    for i in range(len(data)):  # REVIEW THIS SECTION!!
        if data[i][1] is not None:
            index = years.index(data[i][0].year)
            totals[index] += data[i][1]
            counts[index] += 1

    averages = []
    for i in range(len(totals)):
        avg = totals[i] / counts[i]
        averages.append(avg)

    max_index = 0
    for i in range(len(averages)):
        if averages[i] > averages[max_index]:
            max_index = i
    #return years[max_index]

    x_values = []
    y_values = []
    for i in range(len(years)):
        x_values.append(years[i])
    for i in range(len(averages)):
        y_values.append(averages[i])

    plt.plot(x_values, y_values)
    plt.xticks(rotation=45)
    plt.show()


#the longest period of continous rain

def main():
    rain = parse_csv('mt_tabor_rain.txt')
    print(f'The mean is: {round(mean(rain))}')
    print(f'The variance is: {round(variance(rain))}')
    print(f'The day with the most rain: {max_rain(rain)}')
    print(f'The year with the most rain: {most_rain_year(rain)}')

main()



