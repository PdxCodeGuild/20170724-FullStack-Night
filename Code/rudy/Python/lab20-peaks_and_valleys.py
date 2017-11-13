# Lab 20    Peaks and Valleys

        # Visualization of test data:
'''
| Data    |  1 | 2 | 3 | 4 | 5 | 6 | 7 | 6 | 5 | 4 | 5 | 6 | 7 | 8 | 9 | 8 | 7 | 6 | 7 | 8 | 9 |
|---------|----|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Index   |  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|
| POI     |    |   |   |   |   |   | P |   |   | V |   |   |   |   | P |   |   | V |   |   |   |
'''


def peaks(data):
    pop_index_list = []
    pop_list = []
    for i in range(1, len(data)-1):
        if data[i-1] < data[i] and data[i+1] < data[i]:
            pop_index_list.append(i)
    for i in range(len(data)):
        if i in pop_index_list:
            pop_list.append('P')
        else:
            pop_list.append(' ')
    print(pop_index_list)
    return pop_list, pop_index_list


def valleys(data):
    pov_index_list = []
    pov_list = []
    for i in range(1, len(data)-1):
        if data[i-1] > data[i] and data[i+1] > data[i]:
            pov_index_list.append(i)
    for i in range(len(data)):
        if i in pov_index_list:
            pov_list.append('V')
        else:
            pov_list.append(' ')
    print(pov_index_list)
    return pov_list, pov_index_list


def print_sexy(data, pov_list, pov_index_list, pop_list, pop_index_list):
    poi_list = []
    data_str = []
    for i in range(len(data)):
        if i in pop_index_list:
            poi_list.append('P')
        elif i in pov_index_list:
            poi_list.append('V')
        else:
            poi_list.append(' ')
        data_str.append(str(data[i]))
    print('|'.join(data_str))
    print('|'.join(poi_list))


def main():
    data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
    pop_list, pop_index_list = peaks(data)
    pov_list, pov_index_list = valleys(data)
    print_sexy(data, pov_list, pov_index_list, pop_list, pop_index_list)

main()
